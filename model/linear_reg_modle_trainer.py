import os
import pandas as pd
import math
import matplotlib.pyplot as mtp
from sklearn.linear_model import LinearRegression
import pickle

cwd = os.getcwd()
name = "WIPRO"
min = 30

data = pd.read_csv(f'{cwd}/model/dataset/{name}.csv')
data.head()


data['pre-high'] = data['high'].shift(+min)
data['pre-low'] = data['low'].shift(+min)
data['pre-volume'] = data['volume'].shift(+min)
data['pre-open'] = data['open'].shift(+min)
data = data.dropna()
data.head()

X = data[['open','pre-open','pre-high','pre-low','pre-volume']]
Y = data[['close']]

mtp.title("LT prediction")
mtp.ylabel("Close")
mtp.xlabel("Date")
mtp.plot(Y['close'])
mtp.show()

values = Y.values
data_train_size = math.ceil(len(values)*0.8)
print(data_train_size)



Y_train = Y[0:data_train_size]
Y_test = Y[data_train_size:]
print(Y_train)
print(Y_test)


mtp.title("LT")
mtp.ylabel("Close")
mtp.xlabel("Date")
mtp.plot(Y_train['close'])
mtp.plot(Y_test['close'])
mtp.show()

X_train = X[0:data_train_size]
X_test = X[data_train_size:]
print(X_train)
print(X_test)

model = LinearRegression()
model.fit(X_train,Y_train)

with open(f'LT.pickle','wb') as f:
    pickle.dump(model, f)

prediction = model.predict(X_test)
Y_test['predict'] = prediction
print(Y_test)

mtp.title("LT Predict")
mtp.ylabel("Close")
mtp.xlabel("Date")
mtp.plot(Y_train['close'])
mtp.plot(Y_test['close'])
mtp.plot(Y_test['predict'])
mtp.show()