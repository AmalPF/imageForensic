#from django.db import models
#from PIL import Image
import numpy as np

# Create your models here.

"""
class ImageDetails: #(models.Model):
    name : str 
    image_path : str 
"""

class FakeImageDetectionClass:
    model1_name : str 
    model2_name : str 
    model3_name : str 
    model1_output : int 
    model2_output : int 
    model3_output : int 
    model1_color : str 
    model2_color : str 
    model3_color : str 
    color_class: str
    conclusion: str
    error : str

class ImageProperties:
    properties : list 
    histogram : list 
    rgb_graph : dict
    properties_found : bool
    error : str

class ObjectDetectionClass:
    objects : list 
    objects_found : bool
    error : str

