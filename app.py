from flask import Flask, render_template, request
from scrapper import value, data, getStock, getName
from predict import predictPrice, predictPrice2, predictPrice3, predictPrice4, predictPrice5

app = Flask(__name__)

@app.route('/')
def index():
    dict = ['LT', 'TCS', 'HDFC', 'WIPRO', 'INFY']
    interDict = [1,2,3,4,5] 
    stock_code = request.args.get('stock_code',default='LT')
    interval = request.args.get('interval',default='1')
    lt = getStock(stock_code)
    dict.remove(stock_code)
    interDict.remove(int(interval))
    name = getName(stock_code)
    values = value()
    inter = []
    datas = data()

    price = []
    p = [[lt['close'][len(lt)-1],lt['open'][len(lt)-1],lt['volume'][len(lt)-1],lt['high'][len(lt)-1],lt['low'][len(lt)-1]]]
    if(int(interval) > 0):
        temp = predictPrice(stock_code, p)
        price.append(temp)
        values.append("P1")
        inter.append("P1")
        datas.append(temp)
        # p = [[temp,lt['open'][len(lt)-1],lt['volume'][len(lt)-1],lt['high'][len(lt)-1],lt['low'][len(lt)-1]]]
       
    if(int(interval) > 1):
        temp = predictPrice2(stock_code, p)
        price.append(temp)
        values.append("P2")
        inter.append("P2")
        datas.append(temp)
        #p = [[temp,lt['open'][len(lt)-1],lt['volume'][len(lt)-1],lt['high'][len(lt)-1],lt['low'][len(lt)-1]]]

    if(int(interval) > 2):
        temp = predictPrice3(stock_code, p)
        price.append(temp)
        values.append("P3")
        inter.append("P3")
        datas.append(temp)

    if(int(interval) > 3):
        temp = predictPrice4(stock_code, p)
        price.append(temp)
        values.append("P4")
        inter.append("P4")
        datas.append(temp)

    if(int(interval) > 4):
        temp = predictPrice5(stock_code, p)
        price.append(temp)
        values.append("P5")
        inter.append("P5")
        datas.append(temp)

    
    
    return render_template('index.html',dataVal=datas, valueVal=values, code = stock_code, name=name, len=len(dict), dict=dict, data_len=len(datas), predict=price, pricelen = len(price), interval = int(interval), inter = inter, iDict = interDict, ilen = len(interDict))




if __name__ == "__main__":
    app.run(debug=True)