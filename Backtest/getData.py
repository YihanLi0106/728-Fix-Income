import requests
import json
import pandas as pd

from temp import *

a = json.loads(response.content)
data = []
date = []
for i in a:
    data.append(i['mid_price.numeric'])
    date.append(i['date'])

df = pd.DataFrame({'date': date, 'data': data})
df['data'] = df['data'].replace(to_replace=0, method='ffill')
df.to_csv('Spain OBL 2.9% 31oct2046')

import matplotlib.pyplot as plt
plt.plot(df['data'])
plt.show()
print(1)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"items":[{"id":162813,"tgId":32,"model":"bonds"}],"startDate":"2021-04-22","endDate":"2024-04-22","chartType":"price","userChangePeriod":false,"getChartIteration":2}'
#response = requests.post('https://cbonds.com/api/chart/get_tradings/', cookies=cookies, headers=headers, data=data)