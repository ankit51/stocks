from time import sleep
from selenium import webdriver

stock = 'BAJAJ-FIN'

stock_dict = {
    'BAJAJ-FIN': {
        'xpath': '//*[@id="div_bse_livebox_wrap"]/div[1]/div[1]/div/div[2]/span[1]',
        'url': 'https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/bajajfinance/BAF'
}
}


response = webdriver.Chrome('/Users/ankit/Downloads/chromedriver 2')
response.get(stock_dict[stock]['url'])
for i in range(10):
    Element = response.find_element_by_xpath(stock_dict[stock]['xpath'])
    print (Element.text)
    sleep(1)
