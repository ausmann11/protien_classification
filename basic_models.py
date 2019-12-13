###
# THIS FILE CONTAINS STEPS FOR AUTOMATING BASIC MODELS
###

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from skimage.io import imread_collection
from sklearn.decomposition import PCA
import skimage.io as io
from skimage import data_dir

##
# Create training set
##
# Ditylum
image_directory_dit = "/Users/samanthacombs/Documents/Main/FAU/TRAIN/Ditylum/"
img_list_dit = glob.glob(f"{image_directory_dit}*.tif")
# NOT Ditylum
image_directory_not_dit = "/Users/samanthacombs/Documents/Main/FAU/TRAIN/NotDitylum/"
img_list_not_dit = glob.glob(f"{image_directory_not_dit}*.tif")

##
# Fill NA's w/ 0's, adds labels, and flattens image from Ditylum folder
##
df_1 = flat_images(img_list_dit)
df_1 = df_1.fillna(0)
df_1["label"] = 1

# flattens not Ditylum images
df_1 = flat_images(img_list_not_dit)
df_1 = df_1.fillna(0)
df_1["label"] = 1

# puts both sets of images in same dataframe (1st portion is ditylum)
df = df_1.append(df_0)
df.reset_index(inplace=True)
df = df.fillna(0)

##
# Orientation/Rotate (maybe a step we will take)
##

##
# Train/Test Split - sklearn
##
X = df.drop(["label"], axis=1)
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

##
# PCA - run after train/test split
##
pca = PCA()
pca.fit(X_train)
csum = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax(csum >= 0.99) + 1

pca = PCA(n_components=d)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

##
# Run through models
##
