
# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

cnt=0
while cnt<100:
    print(si.get_live_price('ADANIPORTS.NS'))
    cnt+=1