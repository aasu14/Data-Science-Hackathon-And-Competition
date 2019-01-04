from keras.applications.vgg16 import VGG16
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, GlobalAveragePooling2D
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Sequential
from keras.utils import np_utils

import numpy as np 
from numpy import genfromtxt

# Training and test data 
train_file = '../input/train.csv'
test_file = '../input/test.csv'
model_file = '../output/digitrecognizer.model.json'
model_weights_file = '../output/digitrecognizer.model.best.hdf5'

image_size = None

# Load training data from a file and return X, y
def load_training_data(file_name):
    raw_data = genfromtxt(file_name, delimiter=',', skip_header=1)

    raw_sample_image = raw_data[0][1:]
    image_size = int(np.sqrt(len(raw_sample_image)))
    print(image_size)
    X_shape = (len(raw_data), image_size, image_size, 1)
    y_shape = (len(raw_data), 10)

    X_data = np.zeros(X_shape)
    y_data = np.zeros(y_shape)
    for index, datum in enumerate(raw_data):
        X_data[index] = np.array(datum[1:]/255).reshape(image_size, image_size, 1)
        y_data[index] = np_utils.to_categorical(int(datum[0]), 10)        

    return X_data, y_data

print("Loading training data")
X_train, y_train = load_training_data(train_file)


# Build a new model
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=3, padding='same', activation='relu', input_shape=(image_size, image_size, 1)))
model.add(Conv2D(filters=16, kernel_size=3, padding='same', activation='relu'))
model.add(Dropout(0.1))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))
model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(Dropout(0.3))
model.add(GlobalAveragePooling2D())
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Save the model
model_json = model.to_json()
with open(model_file, 'w') as json_file:
    json_file.write(model_json)

# train the model
#model.load_weights(model_weights_file)
checkpointer = ModelCheckpoint(filepath=model_weights_file, verbose=1, save_best_only=True)
stopper = EarlyStopping(monitor='val_loss', min_delta=1e-4, patience=10, verbose=1, mode='auto')
hist = model.fit(X_train, y_train, batch_size=32, epochs=1000, validation_split=0.2, callbacks=[checkpointer, stopper], verbose=1, shuffle=True)

