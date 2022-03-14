import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf 
import os
from PIL import Image
import cv2

import struct
from numpy import expand_dims
from keras.layers import Input, Conv2D, BatchNormalization, LeakyReLU, ZeroPadding2D, UpSampling2D
from keras.layers.merge import add, concatenate
from keras.models import Model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from matplotlib.patches import Rectangle
from imageAnalysis.models import BoundBox, ObjectDetectionClass
#from tensorflow.keras.utils import load_img

from imageForensic.settings import BASE_DIR, STATICFILES_DIRS


YOLO_MODEL_PATH = os.path.join(BASE_DIR,"trained models/YOLO Model.h5")
OUTPUT_DIR = os.path.join(BASE_DIR, "static/media")
model = tf.keras.models.load_model(YOLO_MODEL_PATH)

def object_detection_predictoin(request):
	result = ObjectDetectionClass()
	if request.FILES:
		image_file = request.FILES['image']
		image = Image.open(image_file)

        #file_name = str(image_file)
		image_path = os.path.join(STATICFILES_DIRS[0], "media/input_image.png")
		image.save(image_path)

		print("Image detection function called")
		result = detect_objects(image_path)

		if result.properties == []:
			result.properties_found = False
		else:
			result.properties_found = True 
	else:
		result.error = "Image not found"

	return result


def detect_objects(image_path):
	pass 


def preparing_input():
	image = cv2.imread(args.image)

	Width = image.shape[1]
	Height = image.shape[0]
	scale = 0.00392

# read class names from text file
	classes = None
	with open(args.classes, 'r') as f:
		classes = [line.strip() for line in f.readlines()]

# generate different colors for different classes 
	COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

# read pre-trained model and config file
	net = cv2.dnn.readNet(args.weights, args.config)

# create input blob 
	blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

# set input blob for the network
	net.setInput(blob)