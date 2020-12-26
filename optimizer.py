from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import numpy as np
import time

X = np.load('npys/X1.npy')
y = np.load('npys/y1.npy')

X = X/255.0

DENSE_LAYYERS = [0, 1, 2]
LAYER_SIZES = [32, 64]
CONV_LAYERS = [2, 3]

for dense_layer in DENSE_LAYYERS:
    for layer_size in LAYER_SIZES:
        for conv_layer in CONV_LAYERS:
            NAME = f'{conv_layer}-conv-{layer_size}-nodes-{dense_layer}-dense-{format(int(time.time()))}'

            model = Sequential()

            model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
            model.add(Activation('relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))
            for layer in range(conv_layer-1):
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())

            for layer in range(dense_layer):
                model.add(Dense(dense_layer))
                model.add(Activation('relu'))

            model.add(Dense(1))
            model.add(Activation('sigmoid'))
            
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
            
            model.fit(X, y, batch_size=32, epochs=10, validation_split=0.1)

            model.save(f'MODELS/all_classifier_0/{NAME}')
