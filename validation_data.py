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

X_val = []
y_val = []
X_val.clear()
y_val.clear()
valid_data = pb.read_csv('validation_data\C-NMC_test_prelim_phase_data_labels.csv')

valid_data.head()

for image_name in valid_data.new_names:
    img = imread(f'validation_data\C-NMC_test_prelim_phase_data\{image_name}')
    img = resize(img, (128, 128))
    X_val.append(img)
X_val = np.array(X_val)
y_val = valid_data.labels.values

np.save('X_val.npy', X_val)
np.save('y_val.npy', y_val)
