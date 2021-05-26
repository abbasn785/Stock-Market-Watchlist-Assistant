'''functions'''
from bs4 import BeautifulSoup
import cloudscraper
import re

#gets the top performing sector for the week
def get_sector():
    sector_url = 'https://finviz.com/groups.ashx?g=sector&v=110&o=-perf1w'
    sec_scraper = cloudscraper.create_scraper()
    sec_r = sec_scraper.get(sector_url)
    sec_data = sec_r.text
    sec_soup = BeautifulSoup(sec_data,'html.parser')
    group = sec_soup.find('td', attrs={'height': "10", 'align':'left', 'class': "body-table"})
    sectorOG = group.text
    return sectorOG

#gets the stocks from the criterias given
def get_stocks(urls):
    stonks = {}
    for url in urls.keys():
        assert "screener.ash" in url, "Incorrect URL, please use a url with criteria from https://finviz.com/screener.ashx"
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        s = set()
        pattern = "t=(.*?)&ty"

        for link in soup.find_all('a'):
            x = link.get('href')
            if 'quote' in x:
                stock = re.search(pattern, x).group(1)
                s.add(stock)
        if len(s) > 0:
            stonks[urls[url]] = s
        else:
            stonks[urls[url]] = None

    return stonks

#returns stocks list as a str for use in the larger dictionary
def stocks_as_str(stocks):
    stock_str = ""
    for k,v in stocks.items():
        stock_str += (f"{k}: {v}\n")
    return stock_str

#returns the main str we use for the days listing in the watchlist
def get_main(day, stonks):
    stock_str = stocks_as_str(stonks)
    main_dict = {day: f"{stock_str}"}

    main_str = ""
    for k, v in main_dict.items():
        main_str += (f"{k}: ")
        x = v.split('\n')
        x = x[:-1]
        num = len(day) + 2
        for i in x:
            if x.index(i) != 0:
                main_str += ' '*num + f"{i}\n"
            else:
                main_str += f"{i}\n"
    return main_str
