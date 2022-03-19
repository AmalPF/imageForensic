import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf 
import os
from PIL import Image
from collections import Counter

from imageAnalysis.object_detection_funcions import *
from imageAnalysis.models import ObjectDetectionClass

from imageForensic.settings import BASE_DIR, STATICFILES_DIRS




model = tf.keras.models.load_model(YOLO_MODEL_PATH)
#print(model.summary())

# read weights from yolov3 weights file provided in the data
weight_reader = WeightReader(YOLO_COCO_DATA + '/yolov3.weights')

# set the model weights into the model
weight_reader.load_weights(model)

# loading the coco.names labels
labels = []
with open(YOLO_COCO_DATA +"/coco.names", "r") as f:
	labels = [line.strip() for line in f.readlines()]

def object_detection_predictoin(request):
	result = ObjectDetectionClass()
	if request.FILES:
		image_file = request.FILES['image']
		image = Image.open(image_file)

        #file_name = str(image_file)
		image_path = os.path.join(STATICFILES_DIRS[0], "media/input_image.png")
		image.save(image_path)

		#print("Image detection function called")
		labels = detect_objects(image_path)

		if labels:
			result.objects_found = True
			result.objects = []
			label_count = Counter(labels)

			for key in label_count:
				result.objects.append({"object":key, "count":label_count[key]})
		else:
			result.objects_found = False

	else:
		result.error = "Image not found"

	return result




def detect_objects(image_path):
	global labels
	# define the expected input shape for the model
	input_w, input_h = 416, 416
	# define our new photo
	photo_filename = image_path
	# load and prepare image
	image, image_w, image_h =load_image_pixels(photo_filename, (input_w, input_h))
	# make prediction
	yhat = model.predict(image)
	# summarize the shape of the list of arrays
	#print([a.shape for a in yhat])
	# define the anchors
	anchors = [[116,90, 156,198, 373,326], [30,61, 62,45, 59,119], [10,13, 16,30, 33,23]]
	# define the probability threshold for detected objects
	class_threshold = 0.7
	boxes = list()
	for i in range(len(yhat)):
		# decode the output of the network
		boxes += decode_netout(yhat[i][0], anchors[i], class_threshold, input_h, input_w)
	# correct the sizes of the bounding boxes for the shape of the image
	correct_yolo_boxes(boxes, image_h, image_w, input_h, input_w)
	# suppress non-maximal boxes
	do_nms(boxes, 0.4)
	v_boxes, v_labels, v_scores = get_boxes(boxes, labels, class_threshold)
	
	# draw what we found
	draw_boxes(photo_filename, v_boxes, v_labels, v_scores)
	return v_labels




