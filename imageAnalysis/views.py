from django.shortcuts import render
from PIL import Image
import os

from imageForensic.settings import STATICFILES_DIRS

from imageAnalysis.models import *
from imageAnalysis.template_style import *
from imageAnalysis.analysis import fake_image_detection_prediction
from imageAnalysis.image_properties import image_properties_and_characteristics
from imageAnalysis.object_detection import object_detection_predictoin


#from skimage import resize


# Create your views here.
def index(request):
    return render(request, "index.html")

def fake_image_detection(request):
    return render(request, "fake-image-detection.html")

def image_properties(request):
    return render(request, "image-properties.html")

def object_detection(request):
    return render(request, "object-detection.html")

def about(request):
    return render(request, "about.html")
    
def contact(request):
    return render(request, "contact.html")

def blank(request):
    return render(request, "blank.html")

def page_not_found(request):
    return render(request, "404.html")




def image_analysis_result(request):
    if request.method == "POST":
        
        result1 = image_properties_and_characteristics(request)

        result2 = fake_image_detection_prediction(request)
        
        result3 = object_detection_predictoin(request)

    return render(request, "image-analysis-result.html", { "result1" : result1 , "result2" : result2 , "result3" : result3 })



def fake_image_detection_result(request):
    if request.method == "POST":
        result = fake_image_detection_prediction(request)

    return render(request, "fake-image-detection-result.html", { "result" : result })


def image_properties_result(request):
    if request.method == "POST":
        result = image_properties_and_characteristics(request)
    return render(request, "image-properties-result.html", { "result" : result })


def object_detection_result(request):
    result = ObjectDetectionClass()
    if request.method == "POST":
        result = object_detection_predictoin(request)

    return render(request, "object-detection-result.html", { "result" : result })


