#%%
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

filepath = r'C:\Users\User\Pictures\Wedding Photos'.replace('\\', '/')

scale = .5

for im in os.listdir(filepath):
    image = cv2.imread(filepath + '/' + im)
    new_size = (int(scale * image.shape[1]), int(scale * image.shape[0]))
    cv2.imwrite(filepath + '/Resized/' + im.split('.')[0] + '_resized.jpg',
                cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC))







