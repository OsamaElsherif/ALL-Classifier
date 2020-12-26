import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import random
import pickle


# Contant variables
DATASET = 'training_data/fold_2'
CATAGORIES = ['all', 'hem']
IMG_SIZE = 128
training_data = []


# creating training data list
def create_training_data():
    for catagory in CATAGORIES:
        path = os.path.join(DATASET, catagory)
        class_numper = CATAGORIES.index(catagory)
        print(path)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_numper])
            except Exception as e:
                pass


create_training_data()
# print(len(training_data))
random.shuffle(training_data)

X = [] # list which will have imgs in it
y = [] # list which will have categories labels in it

# appending the data
for feat, cat in training_data:
    X.append(feat)
    y.append(cat)

# converting the list into numpy array
X = np.array(X).reshape(-1 ,IMG_SIZE, IMG_SIZE, 3)

# save the training dataset information in a file
np.save('X3.npy', X)
np.save('y3.npy', y)

