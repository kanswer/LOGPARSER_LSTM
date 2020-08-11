import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

import GetData

x_train_data,y_train_data=GetData.GetData('D:\SIT_PROJECT\LogParser_LSTM\EventSequence')
model=keras.Sequential([
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(133)
])
model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])
model.fit(x_train_data,y_train_data,epochs=10)