
import requests
from lxml import html

nifty50 = {'adaniportsspecialeconomiczone': 'https://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/adaniportsspecialeconomiczone/MPS',
 'asianpaints': 'https://www.moneycontrol.com/india/stockpricequote/paintsvarnishes/asianpaints/AP31',
 'axisbank': 'https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/axisbank/AB16',
 'bajajauto': 'https://www.moneycontrol.com/india/stockpricequote/auto23wheelers/bajajauto/BA10',
 'bajajfinance': 'https://www.moneycontrol.com/india/stockpricequote/financeleasinghirepurchase/bajajfinance/BAF',
 'bajajfinserv': 'https://www.moneycontrol.com/india/stockpricequote/financeinvestments/bajajfinserv/BF04',
 'bhartiairtel': 'https://www.moneycontrol.com/india/stockpricequote/telecommunicationsservice/bhartiairtel/BA08',
 'bhartiinfratel': 'https://www.moneycontrol.com/india/stockpricequote/telecommunicationsequipment/bhartiinfratel/BI14',
 'bharatpetroleumcorporation': 'https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC',
 'britanniaindustries': 'https://www.moneycontrol.com/india/stockpricequote/foodprocessing/britanniaindustries/BI',
 'cipla': 'https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/cipla/C',
 'coalindia': 'https://www.moneycontrol.com/india/stockpricequote/miningminerals/coalindia/CI11',
 'drreddyslaboratories': 'https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/drreddyslaboratories/DRL',
 'eichermotors': 'https://www.moneycontrol.com/india/stockpricequote/autolcvshcvs/eichermotors/EM',
 'gailindia': 'https://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/gailindia/GAI',
 'grasimindustries': 'https://www.moneycontrol.com/india/stockpricequote/diversified/grasimindustries/GI01',
 'hcltechnologies': 'https://www.moneycontrol.com/india/stockpricequote/computerssoftware/hcltechnologies/HCL02',
 'housingdevelopmentfinancecorporation': 'https://www.moneycontrol.com/india/stockpricequote/financehousing/housingdevelopmentfinancecorporation/HDF',
 'hdfcbank': 'https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/hdfcbank/HDF01',
 'heromotocorp': 'https://www.moneycontrol.com/india/stockpricequote/auto23wheelers/heromotocorp/HHM',
 'hindalcoindustries': 'https://www.moneycontrol.com/india/stockpricequote/aluminium/hindalcoindustries/HI',
 'hindustanunilever': 'https://www.moneycontrol.com/india/stockpricequote/personalcare/hindustanunilever/HU',
 'icicibank': 'https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/icicibank/ICI02',
 'indusindbank': 'https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/indusindbank/IIB',
 'infosys': 'https://www.moneycontrol.com/india/stockpricequote/computerssoftware/infosys/IT',
 'indianoilcorporation': 'https://www.moneycontrol.com/india/stockpricequote/refineries/indianoilcorporation/IOC',
 'itc': 'https://www.moneycontrol.com/india/stockpricequote/cigarettes/itc/ITC',
 'jswsteel': 'https://www.moneycontrol.com/india/stockpricequote/steellarge/jswsteel/JSW01',
 'kotakmahindrabank': 'https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/kotakmahindrabank/KMB',
 'larsentoubro': 'https://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/larsentoubro/LT',
 'mahindramahindra': 'https://www.moneycontrol.com/india/stockpricequote/autocarsjeeps/mahindramahindra/MM',
 'marutisuzukiindia': 'https://www.moneycontrol.com/india/stockpricequote/autocarsjeeps/marutisuzukiindia/MS24',
 'nestleindia': 'https://www.moneycontrol.com/india/stockpricequote/foodprocessing/nestleindia/NI',
 'ntpc': 'https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/ntpc/NTP',
 'oilnaturalgascorporation': 'https://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/oilnaturalgascorporation/ONG',
 'powergridcorporationindia': 'https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/powergridcorporationindia/PGC',
 'relianceindustries': 'https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI',
 'statebankindia': 'https://www.moneycontrol.com/india/stockpricequote/bankspublicsector/statebankindia/SBI',
 'shreecements': 'https://www.moneycontrol.com/india/stockpricequote/cementmajor/shreecements/SC12',
 'sunpharmaceuticalindustries': 'https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI',
 'tatamotors': 'https://www.moneycontrol.com/india/stockpricequote/autolcvshcvs/tatamotors/TM03',
 'tatasteel': 'https://www.moneycontrol.com/india/stockpricequote/steellarge/tatasteel/TIS',
 'tataconsultancyservices': 'https://www.moneycontrol.com/india/stockpricequote/computerssoftware/tataconsultancyservices/TCS',
 'techmahindra': 'https://www.moneycontrol.com/india/stockpricequote/computerssoftware/techmahindra/TM4',
 'titancompany': 'https://www.moneycontrol.com/india/stockpricequote/miscellaneous/titancompany/TI01',
 'ultratechcement': 'https://www.moneycontrol.com/india/stockpricequote/cementmajor/ultratechcement/UTC01',
 'upl': 'https://www.moneycontrol.com/india/stockpricequote/chemicals/upl/UP04',
 'vedanta': 'https://www.moneycontrol.com/india/stockpricequote/miningminerals/vedanta/SG',
 'wipro': 'https://www.moneycontrol.com/india/stockpricequote/computerssoftware/wipro/W',
 'zeeentertainmententerprises': 'https://www.moneycontrol.com/india/stockpricequote/mediaentertainment/zeeentertainmententerprises/ZEE'}

stock_dict = {
        'price-xpath': '//*[@id="div_nse_livebox_wrap"]/div[1]/div[1]/div/div[2]/span[1]',
        'vol-xpath': '//*[@id="div_nse_livebox_wrap"]/div[1]/div[1]/div/div[3]/span[3]'
}

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

cnt=0
while (cnt < 10):
    for ticker in nifty50:
        pageContent=s.get(nifty50[ticker])
        tree = html.fromstring(pageContent.content)

        price = tree.xpath(stock_dict['price-xpath'])[0].text
        volume = tree.xpath(stock_dict['vol-xpath'])[0].text

        print ('Ticker:', ticker, 'Price:', price, '          Volume:', volume)
    cnt+=1