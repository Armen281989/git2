from bs4 import BeautifulSoup
import requests

corona_url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(corona_url)
soup = BeautifulSoup(r.text,'html.parser')
data = soup.find_all('div',class_ = 'maincounter-number' )
data2 = soup.find_all('div',class_ = 'main_table_countries_div' )

print('Total Cases:', data[0].text.strip())
print('Total Deaths:', data[1].text.strip())
print('Total Recovered:', data[2].text.strip())
armenia = data2[0].text.strip()
count = armenia.index('Armenia')	
print('Country:' + armenia[count:count + 7])
print('Total Cases in Armenia: '+ armenia[count+8:count+11])
print('Total Deaths in Armenia: '+ armenia[count+16:count+18])
print('Total Recovered in Armenia: '+ armenia[count+23:count+26])
