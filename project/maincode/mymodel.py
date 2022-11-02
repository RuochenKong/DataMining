import os
import math
import numpy as np
import pandas as pd
from cnn2L import cnn1
from cnn4L import cnn2


choices = ['norm','origin','filter']

path = {'norm':'normalized', 'origin':'processed_train', 'filter': 'norm_filtcorr'}

dataform = choices[2]


X_train = np.load('../results/keras_%s/xtrain.npy'%dataform)
y_train = np.load('../results/keras_%s/ytrain.npy'%dataform)
X_test = np.load('../results/keras_%s/xtest.npy'%dataform)
y_test = np.load('../results/keras_%s/ytest.npy'%dataform)

feature_length = len(X_train[0])
num_classes = 19

input_shape = (feature_length,1)

X_train = X_train.reshape(len(X_train),feature_length,1)
X_test = X_test.reshape(len(X_test),feature_length,1)


outpath = '../results/keras_%s/'%dataform
if not os.path.exists(outpath):
  os.makedirs(outpath)

model = cnn1(input_shape)
model.summary()


print("Start training the model...")


epochs = 20
batch_size = 128

model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.15)


#model.save('%smodel'%outpath)

print('\nTest Result...')
_,acc = model.evaluate(X_test, y_test, batch_size=batch_size)


'''
f = open('%sacc.txt'%outpath,'w')
f.write('%.4f'%acc)
f.close()

pred = model.predict(X_test)
np.save('%syhat.npy'%outpath,np.array(pred))
'''