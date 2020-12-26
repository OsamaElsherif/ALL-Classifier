import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pb
import cv2
import os
import random
import pickle
from skimage.io import imread, imshow
from skimage.transform import resize
from sklearn.utils import shuffle

DATASETS = []
AF = []
HF = []
A = []
H = []
X = []
y = []
DATASETS.clear()
A.clear()
H.clear()
CATAGORIES = ['all', 'hem']
IMG_SIZE = 128
training_data = []
valid_data = pb.read_csv('validation_data\C-NMC_test_prelim_phase_data_labels.csv')
print('intiating...')

for fold in os.listdir('training_data'):
    print('getting folds')
    for sub in os.listdir(f"training_data\{fold}"):
        DATASETS.append(f'training_data\{fold}\{sub}')
#print(DATASETS)
i = 0
for DATASET in DATASETS:
    print('getting paths')
    if i == len(DATASETS):
        pass
    else:
        if i%2:
            HF.append(DATASET)
            i += 1
        else:
            AF.append(DATASET)
            i += 1
#print(AF)
#print(HF)

for folder in AF:
    print('appending folders')
    for img in os.listdir(folder):
        A.append(f'{folder}\{img}')

for folder in HF:
    print('appending folders')
    for img in os.listdir(folder):
        H.append(f'{folder}\{img}')

print('creating')
for i in range(0, len(A)):
    img = imread(A[i])
    img = resize(img, (128, 128))
    X.append(img)
    y.append(1)

for i in range(0, len(H)):
    img = imread(H[i])
    img = resize(img, (128, 128))
    X.append(img)
    y.append(0)

X = np.array(X)
y = np.array(y)

#X.shape, y.shape

X, y = shuffle(X, y, random_state = 42)

np.save('X.npy', X)
np.save('y.npy', y)

def test():
    fig, ax = plt.subplots(nrows = 1, ncols = 5, figsize = (20, 20))
    for i in range(0, 5):
        rand = np.random.randint(len(X))
        ax[i].imshow(X[rand])
        ax[i].axis('off')
        a = y[rand]
        if a == 1:
            ax[i].set_title('Diseased')
        else:
            ax[i].set_title('non')
