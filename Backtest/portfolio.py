# import os
import pandas as pd
from trading_dates import *
# files = os.listdir('./price')
# print(files)
temp = pd.read_csv('modest.csv')
for w in temp['weights']:
    values_list = w.strip('[]').split()
    float_values = [float(val) for val in values_list]
    print(w)
files = ['USA Notes 2.625% 31mar2025', 'USA Notes 1.25% 31dec2026', 'USA Notes 0.625% 31dec2027',
         'USA Bonds 3.25% 15may2042', 'USA Bonds 3% 15aug2052', 'Freddie Mac 0.375% 23sep2025',
         'New South Wales Treasury Corp 3% 20may2027', 'Western Australian Treasury Corporation (WATC) 3.25% 20jul2028',
         'New South Wales Treasury Corp 2.25% 7may2041', 'Belgium OLO 3.75% 22jun2045', 'Japan JGB 0.4% 20sep2025',
         'Japan JGB 0.1% 20sep2027', 'Japan JGB 0.1% 20jun2031', 'Japan JGB 1% 20dec2035', 'Japan JGB 1.7% 20sep2044',
         'Spain OBL 3.8% 30apr2024', 'Spain OBL 2.15% 31oct2025', 'Spain OBL 1.45% 31oct2027',
         'Spain OBL 2.35% 30jul2033', 'Spain OBL 2.9% 31oct2046']

localData1 = {}
dailyLineDict = {}
# temp = pd.read_pickle('localData')
for i in files:
    data = pd.read_csv('./price/' + i)
    data = data[data['date'].apply(lambda x: len(x) <= 10)]
    data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y')
    dates = pd.DataFrame({'date': get_trading_dates('2022-09-21', '2024-04-25')})
    data = data[data['date'] >= pd.to_datetime('2022-09-21')]
    data = data[data['date'] <= pd.to_datetime('2024-04-25')]
    data['date'] = data['date'].apply(lambda x: str(x)[0:10])
    data = pd.merge(dates, data, how='left')
    data['data'] = data['data'].fillna(method='ffill')
    data['data'] = data['data'].fillna(method='bfill')
    dailyLineDict[i] = pd.DataFrame(data={'Open': data['data'].tolist(), 'Close': data['data'].tolist(), 'Volume': [1]*len(data)},
                                    index=data['date'])
localData1['dailyLineDict'] = dailyLineDict
localData1['minTickDict'] = 0.01
localData1['version'] = ['2022-09-21', '2024-04-25', '2024-04-25']
pd.to_pickle(localData1, 'localData')
