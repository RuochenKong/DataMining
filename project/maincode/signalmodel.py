import math
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from resnet import resnet_34

X = np.load('../data/audio.npy')
y = np.load('../data/train_labels.npy')[:5000]

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

train_dataset = tf.data.Dataset.from_tensor_slices((X_train,y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))

model = resnet_34()

epochs = 10
batch_size = 64

model.fit(train_dataset,batch_size=batch_size, epochs=epochs, validation_split=0.15)

model.save('../results/sig/model')

print('\nTest Result...')
_,acc = model.evaluate(test_dataset, batch_size=batch_size)


f = open('../results/sig/acc.txt','w')
f.write('%.4f'%acc)
f.close()

pred = model.predict(X_test)
np.save('../results/sig/yhat.npy',np.array(pred))