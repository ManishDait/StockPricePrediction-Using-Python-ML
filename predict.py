import pickle

def predictPrice(stock_code, data):
    regration = pickle.load(open(f'model/pickles/{stock_code}_5.pickle', 'rb'))
    prediction = regration.predict(data)
    return round(prediction[0][0],2)

def predictPrice2(stock_code, data):
    regration = pickle.load(open(f'model/pickles/{stock_code}_10.pickle', 'rb'))
    prediction = regration.predict(data)
    return round(prediction[0][0],2)

def predictPrice3(stock_code, data):
    regration = pickle.load(open(f'model/pickles/{stock_code}_15.pickle', 'rb'))
    prediction = regration.predict(data)
    return round(prediction[0][0],2)

def predictPrice4(stock_code, data):
    regration = pickle.load(open(f'model/pickles/{stock_code}_20.pickle', 'rb'))
    prediction = regration.predict(data)
    return round(prediction[0][0],2)

def predictPrice5(stock_code, data):
    regration = pickle.load(open(f'model/pickles/{stock_code}_25.pickle', 'rb'))
    prediction = regration.predict(data)
    return round(prediction[0][0],2)
