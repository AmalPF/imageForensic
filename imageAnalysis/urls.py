from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("fake-image-detection/", views.fake_image_detection, name="fakeImageDetection"),
    path("image-properties/", views.image_properties, name="imageProperties"),
    path("object-detection/", views.object_detection, name="objectDetection"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blank/", views.blank, name="blank"),
    path("404/", views.page_not_found, name="404"),

    path("image-analysis-result/", views.image_analysis_result, name="imageAnalysisResult"),
    path("fake-image-detection-result/", views.fake_image_detection_result, name="fakeImageDetectionResult"),
    path("object-detection-result/", views.object_detection_result, name="objectDetectionResult"),
    path("image-properties-result/", views.image_properties_result, name="iamgePropertiesResult")
]