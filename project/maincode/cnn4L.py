import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, BatchNormalization
from keras.layers.convolutional import Conv1D, MaxPooling1D

def cnn2(input_shape):
	model = Sequential()
	model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=input_shape))
	model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
	model.add(Dropout(0.5))

	model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
	model.add(Conv1D(filters=256, kernel_size=2, activation='relu'))
	model.add(MaxPooling1D(pool_size=2))
	model.add(BatchNormalization())
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(500, activation='relu'))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(19, activation='softmax'))
	model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	return model