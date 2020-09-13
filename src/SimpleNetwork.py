import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

import GetData_pro

x_train_data,y_train_data=GetData_pro.GetData()
x_train_data=np.reshape(x_train_data,(len(x_train_data),3,1))
x_train_data=x_train_data/float(132)
y_train_data=keras.utils.to_categorical(y_train_data)

model=keras.Sequential([
    #keras.layers.Dense(250,activation='relu'),
    keras.layers.LSTM(32,input_shape=(x_train_data.shape[1],x_train_data.shape[2])),
    keras.layers.Dense(y_train_data.shape[1],activation='softmax')
])
model.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])
model.fit(x_train_data,y_train_data,epochs=500,batch_size=1)

test_loss,test_acc=model.evaluate(x_train_data,y_train_data,verbose=0)
print('\nTest accuracy:',test_acc)