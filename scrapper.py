from tvDatafeed import TvDatafeed, Interval
from datetime import datetime
  
tv = TvDatafeed()
lt = ''

def getStock(stock_code):
     global lt
     lt = tv.get_hist(symbol=stock_code, exchange="NSE", interval=Interval.in_5_minute, n_bars=75)
     print(lt)
     return lt

def getName(stock_code):
    dict = {'LT':'Larsen and Tuplo', 'TCS':'Tata Consultency and Services', 'HDFC':'Housing Development Finance Corporation Limited', 'WIPRO':'Wipro Limited', 'INFY':'Infosys Limited'}
    return dict[stock_code]


def data():
   
    list =lt['close']
    data = []
    
    for i in range(len(list)):
        data.append(list[i])
    
    return data

def value():
    list = lt.index
    value = []

    for i in range(len(list)):
        val = str(list[i])
        val = val.split()[1]
        #['2023-02-27','11:50:00']
        t = f"{val.split(':')[0]}:{val.split(':')[1]}"
        #[11,50,00]
        time = datetime.strptime(t,"%H:%M")
        time = time.strftime("%I:%M %p")
        value.append(time)

    return value





