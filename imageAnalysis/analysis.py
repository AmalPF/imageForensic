import numpy as np
import os
import tensorflow as tf
from skimage import io
from skimage.transform import resize
from PIL import Image

from imageAnalysis.models import FakeImageDetectionClass
from imageForensic.settings import BASE_DIR, STATICFILES_DIRS


# loading the trained models
model_path1 = os.path.join(BASE_DIR,"trained models/mobilenetV2 model.h5")
trained_model1 = tf.keras.models.load_model(model_path1)

model_path2 = os.path.join(BASE_DIR,"trained models/inceptionv3 model.h5")
trained_model2 = tf.keras.models.load_model(model_path2)

model_path3 = os.path.join(BASE_DIR,"trained models/vgg16 model.h5")
trained_model3 = tf.keras.models.load_model(model_path3)


# analysis functions    

def fake_image_detection_prediction(request):
    result = FakeImageDetectionClass
    if request.FILES:
        input_image = request.FILES['image']
        image = Image.open(input_image)
        image_path = os.path.join(STATICFILES_DIRS[0], "media/input_image.png")
        image.save(image_path)

        image_arr = image_preprocess(input_image)

        name1, output1 = mobilenetv2_model(image_arr)
        name2, output2 = inceptionv3_model(image_arr) 
        name3, output3 = vgg16_model(image_arr) 

        color_class1 = "success" if output1 < 50 else "danger"
        color_class2 = "success" if output2 < 50 else "danger"
        color_class3 = "success" if output3 < 50 else "danger"

        result.model1_name, result.model1_output = name1, output1
        result.model2_name, result.model2_output = name2, output2
        result.model3_name, result.model3_output = name3, output3
        result.model1_color = color_class1 
        result.model2_color = color_class2
        result.model3_color = color_class3 

        total_percentage = output1 + output2 + output3 

        if total_percentage < 150:
            result.conclusion = "Real Image"
            result.color_class = "text-success"
        else:
            result.conclusion = "Fake Image"
            result.color_class = "text-danger"
    else:
        result.error = "Image not found"

    return result



def image_preprocess(input_image):
    image = io.imread(input_image)
    #image.save('input image.png')

    image =  resize(image, (224,224,3), anti_aliasing=True) 
    #print("Image size : ", image.size)

    image_arr = np.array([image])
    #print("Image array size : ", image_arr.shape)

    return image_arr 



def mobilenetv2_model(x):
    global trained_model1 
    #print(trained_model1.summary())

    y_pred = trained_model1.predict(x)
    #print("Model 1 prediction : ", y_pred)

    y_pred = int(100 - y_pred[0][0] * 100)
    return "MobileNetV2 Model", y_pred



def inceptionv3_model(x):
    global trained_model2
    #print(trained_model2.summary())

    y_pred = trained_model2.predict(x)
    #print("Model 2 prediction : ", y_pred) 

    y_pred = int(100 - y_pred[0][0] * 100)
    return "InceptionV3 Model", y_pred



def vgg16_model(x):
    global trained_model3
    #print(trained_model3.summary())

    y_pred = trained_model3.predict(x)
    #print("Model 3 prediction : ", y_pred) 

    y_pred = int(100 - y_pred[0][0] * 100)
    return "VGG16 Model", y_pred