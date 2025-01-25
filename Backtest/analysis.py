import os
import pandas as pd
import matplotlib.pyplot as plt

dd = []
v = []
lam = []
for i in os.listdir('./results1'):
    # data = pd.read_csv('./results/' + i + '/netValue&Slippage0.csv', index_col=0)
    # plt.plot(pd.to_datetime(data.index), data.pnl, label=i)
    data = pd.read_csv('./results/' + i + '/performance&Slippage0.csv')
    lam.append(float(i.replace('lambda', '')))
    v.append(data['stddev(annual)'][0])
    dd.append(data['maxDrawdown'][0])

temp = pd.DataFrame({'lam': lam, 'dd': dd, 'v': v})
temp.sort_values(by='lam', ascending=True, inplace=True)
fig, ax1 = plt.subplots()

color1 = 'tab:red'
ax1.set_xlabel('lambda')
ax1.set_ylabel('max drawdown', color=color1)
line1, = ax1.plot(temp['lam'], temp['dd'], color=color1, label='draw down')  # 添加label参数
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()

color2 = 'tab:blue'
ax2.set_ylabel('volatility', color=color2)
line2, = ax2.plot(temp['lam'], temp['v'], color=color2, label='volatility')  # 添加label参数
ax2.tick_params(axis='y', labelcolor=color2)

lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')  # 设置图例的位置

fig.tight_layout()  # 这会自动调整子图参数，使之填充整个图像区域
plt.show()