###
# THIS FILE CONTAINS STEPS FOR AUTOMATING DEEP LEARNING MODELS
###

# Import libraries from Keras.
import os
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd
import split_folders
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from skimage.io import imread_collection
from sklearn.decomposition import PCA

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import preprocessing
from tensorflow.keras import models
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.models import Sequential
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

##
# Create training set
##

# Ditylum
image_directory_dit = "/Users/smann/Documents/Main/FAU/TRAIN/Ditylum/"
img_list_dit = glob.glob(f"{image_directory_dit}*.tif")
# NOT Ditylum
image_directory_not_dit = "/Users/smann/Documents/Main/FAU/TRAIN/NotDitylum/"
img_list_not_dit = glob.glob(f"{image_directory_not_dit}*.tif")


##
# Train/Test Split or Train/Validation/Test Split (pick 1)
##
training_folder = "/Users/smann/Documents/Main/FAU/TRAIN/"
output_folder = "/Users/smann/Documents/Main/FAU/TestTrain"
train_validation_test_split(training_folder, output_folder)
train_test_split(training_folder, output_folder)

##
# Run through Keras Models...
##

##
# Model Metric Plots
##

# summarize history for accuracy
plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.title("model accuracy")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
plt.show()

# summarize history for loss
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("model loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
plt.show()
