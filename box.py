import matplotlib.pyplot as plt
import numpy as np
from skimage import io, img_as_float
from skimage.feature import blob_log
from scipy.ndimage import gaussian_filter
from skimage.morphology import reconstruction
from skimage.io import imread_collection
import pandas as pd

# from functions import *
from boxsdk import Client
import os
import glob
from PIL import Image
from sklearn.decomposition import PCA

# NEED TO RUN configuration/auth.py to get Box up and running and functions.py to access functions

##
# BOX API - get at all the images that exist in a box folder
##

# TIP: folder id is located at the end of the URL for the folder (https://app.box.com/folder/89393519067)
# Ditylum
folder_id_dit = "90416014352"
output_directory_dit = "/Users/smann/Documents/Main/FAU/TRAIN/Ditylum/"
download_images(folder_id_dit, output_directory_dit)
# Not Ditylum
folder_id_not_dit = "90415600905"
output_directory_not_dit = "/Users/smann/Documents/Main/FAU/TRAIN/NotDitylum/"
download_images(folder_id_not_dit, output_directory_not_dit)

##
# Create training set
##
# Ditylum
image_directory_dit = "/Users/smann/Documents/Main/FAU/TRAIN/Ditylum/"
img_list_dit = glob.glob(f"{image_directory_dit}*.tif")
# NOT Ditylum
image_directory_not_dit = "/Users/smann/Documents/Main/FAU/TRAIN/NotDitylum/"
img_list_not_dit = glob.glob(f"{image_directory_not_dit}*.tif")
training_output_directory = "/Users/smann/Documents/Main/FAU/TRAIN"
training_set(img_list_dit, training_output_directory)
training_set(img_list_not_dit, training_output_directory)
