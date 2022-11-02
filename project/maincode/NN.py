import math
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.layers.convolutional import Conv1D, MaxPooling1D



class Antirectifier(layers.Layer):
    def __init__(self, initializer="he_normal", **kwargs):
        super(Antirectifier, self).__init__(**kwargs)
        self.initializer = keras.initializers.get(initializer)

    def build(self, input_shape):
        output_dim = input_shape[-1]
        self.kernel = self.add_weight(
            shape=(output_dim * 2, output_dim),
            initializer=self.initializer,
            name="kernel",
            trainable=True,
        )

    def call(self, inputs):
        inputs -= tf.reduce_mean(inputs, axis=-1, keepdims=True)
        pos = tf.nn.relu(inputs)
        neg = tf.nn.relu(-inputs)
        concatenated = tf.concat([pos, neg], axis=-1)
        mixed = tf.matmul(concatenated, self.kernel)
        return mixed

    def get_config(self):
        # Implement get_config to enable serialization. This is optional.
        base_config = super(Antirectifier, self).get_config()
        config = {"initializer": keras.initializers.serialize(self.initializer)}
        return dict(list(base_config.items()) + list(config.items()))

labels = np.load('../data/train_labels.npy')
df = pd.read_csv('../data/normalized.csv')

df['label'] = labels


feature_length = len(df.columns) - 1
num_classes = 19

input_shape = (feature_length,)


dfshuffel = df.sample(frac=1)
trainum = int(len(dfshuffel) * 0.8)
X_train = df.iloc[:trainum]
X_test = df.iloc[trainum:]

'''
trainum = int(len(drest) * 0.8)
train = drest[:trainum]
valid = drest[trainum:]
'''

print("Start training the model...")

y_train = X_train.pop('label')
train_dataset = tf.data.Dataset.from_tensor_slices((X_train.values, y_train.values))


y_test = X_test.pop('label')
test_dataset = tf.data.Dataset.from_tensor_slices((X_test.values, y_test.values))


model = keras.Sequential(
    [
        keras.Input(shape=(feature_length,)),
        layers.Dense(256),
        Antirectifier(),
        layers.Dense(256),
        Antirectifier(),
        layers.Dropout(0.5),
        layers.Dense(19),
    ]
)

# Compile the model
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)

batch_size = 128
epochs = 250


# Train the model
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.15)


print('\nTest Result...')
# Test the model
model.evaluate(X_test, y_test)