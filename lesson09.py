
import pandas as pd

table = [
    [52.4800551788,83.6467142857],
    [51.4800551788,85.6467142857],
    [59.4800551788,87.6467142857],
    [55.4800551788,89.6467142857],
    [57.4800551788,80.6467142857]
]
df = pd.DataFrame(table,columns = ['pm25','pm10'])
print(df.sort_index(axis = 1, ascending=False))

#

url = 'http://data.tainan.gov.tw/dataset/1b89994d-ab2a-4126-ab1e-ed1a0cfaeb27/resource/f169b4d7-11d7-400e-b061-249cf9a2bf34/download/1070612tnhp.csv'
data = pd.read_csv(url)
print (data.info)
print (data.shape)
print (data.describe())
print (data.columns)
print (type(data.columns))
print (data.notnull())
print (data.isnull())
# new_data = data.fillna(1324)

#

from requests_html import HTMLSession
session = HTMLSession()
response = session.get('http://quotes.toscrape.com/')

elements = response.html.find('.quote div a', first = True)
# for element in elements :
print(elements.attrs['href'])

# session2 = HTMLSession()
# response2 = session2.get('http://quotes.toscrape.com/')
# elements2 = response2.html.find('.text')
# for element in elements2:
#     print(element.text)

#

import pandas as pd

table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]

df = pd.DataFrame(table, columns = ['class', 'name', 'math_score', 'eng_score'])
print (df)
df_sum = df.groupby('class').sum()
df_mean = df.groupby('class').mean()
print(df_sum)
print(df_mean)
df_corr = df.groupby('class').corr()
print(df_corr)


#

import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute areas and colors
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
plt.show()

#

# import matplotlib.pyplot as plt
# import pandas as pd
# url = 'http://markets.financialcontent.com/stocks/action/gethistoricaldata?Month=12&Symbol=GOOG&Range=300&Year=2017'
# google_stock = pd.read_csv(url)
# new_google_stock = google_stock.iloc[::-1] # 因為收到的資料是從 12/29/17 開始到 03/28/14，因此要轉個方向變成3/28/14到12/29/17。
# new_google_stock = new_google_stock[:30] # 為了讓上下間距區域變明顯，我們只看前面30天的資料
# plt.figure(figsize=(10, 5))

# x = range (0, new_google_stock.shape[0])
# y = new_google_stock['Open']
# y1 = new_google_stock['Low']
# y2 = new_google_stock['High']

# plt.fill_between(x, y1, y2)
# plt.plot(x, y, color='blue', linewidth=2.0, linestyle=':')
# plt.show()

#

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0,1,5)
# y = np.exp(x)
# plt.hist(x,y)
# plt.show()