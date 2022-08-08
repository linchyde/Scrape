#web scraper
import requests
from bs4 import BeautifulSoup
import pprint #allows a more formatted print to the terminal of the data
from dateutil import parser

# text = '<class="dfx-singleForecastBlock__articleDate dfx-font-size-2 dfx-font-size-xl-3 text-muted my-1" data-time="2022-07-30T20:00:00+00:00" data-format-date="getFullDatePlusTZ">'
# souptime = BeautifulSoup(text, features="lxml")
# for t in souptime.find_all('time', attrs={'class': 'data-format-date'}):
#     date_time_str = t.get('data-time')
#     date_time = parser.parse(date_time_str)
#     print(date_time)

#below function is unused only included for future examples
#here we could use a list of extracted data and then sort out output based on a certain attribute
def sort_data_by_undefined(fakelist):
    return sorted(fakelist, key=lambda k:k['data'])


res = requests.get('https://www.dailyfx.com/forecasts')
res2 = requests.get('https://www.dailyfx.com/gold-price/news-and-analysis')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

forecast_links = soup.select('.dfx-singleForecastBlock__articleTitle')
datetime = soup.select('.dfx-singleForecastBlock__articleDate')

gold_links = soup2.select('.dfx-widget__heading font-weight-bold h5 text-black text-uppercase')
datetime2 = soup2.select('.dfx-articleListItem__date')

all_links = forecast_links + gold_links
all_dates = datetime2 + datetime



def create_custom_ff(all_links): #getting the latest forecast links from the site
    ff = [] #empty list to hold the data
    for index, item in enumerate(all_links): #once we have links loop through and get titles and href
        title = all_links[index].getText()
        # print(all_links)
        href = all_links[index].get('href')
        date = all_dates[index].get('data-time')
        ff.append({'title': title, 'link': href, 'date': date}) #append these to a new dictionary
    return ff
# print(datetime)
pprint.pprint(create_custom_ff(all_links))




