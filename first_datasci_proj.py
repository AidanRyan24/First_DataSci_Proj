import requests 
import bs4
import pandas as pd

#get data
result = requests.get('https://www.worldometers.info/coronavirus/country/india/')

#get specifc data
soup = bs4.BeautifulSoup(result.text, "lxml")
cases = soup.find_all('div', class_='maincounter-number')

#store data
data = []

for i in cases:
    span = i.find('span')
    data.append(span.string)

print(data)


# Creating dataframe
df = pd.DataFrame({"CoronaData": data})
 
# Naming the columns
df.index = ['TotalCases', ' Deaths', 'Recovered']

# Exporting data into Excel
df.to_csv('Corona_Data.csv')