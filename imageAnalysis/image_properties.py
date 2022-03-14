from PIL.ExifTags import TAGS
import cv2
from PIL import Image
import os
from collections import Counter

from imageAnalysis.models import ImageProperties
from imageForensic.settings import STATICFILES_DIRS


def image_properties_and_characteristics(request):
    result = ImageProperties()
    if request.FILES:
        image_file = request.FILES['image']
        image = Image.open(image_file)

        #file_name = str(image_file)
        image_path = os.path.join(STATICFILES_DIRS[0], "media/input_image.png")
        image.save(image_path)

        result.properties = image_meta_data(image)
        result.histogram = pixel_intensity_values(image_path)
        result.rgb_graph = rgb_channel_values(image_path)
        print(result.rgb_graph)

        if result.properties == []:
            result.properties_found = False
        else:
            result.properties_found = True 
    else:
        result.error = "Image not found"

    return result



def image_meta_data(image):
    exifdata = image.getexif()
    data = []
    for tag_id in exifdata:
        #if tag_id in TAGS:
            tag = TAGS.get(tag_id, tag_id)
            temp = exifdata.get(tag_id)
            data.append({"tag":tag, "data":temp})
    #print(data)
    return data 


def pixel_intensity_values(image):
    image_arr = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    arr = Counter(image_arr.ravel())
    res_arr = []
    for i in range(256):
        res_arr.append(arr.get(i, 0))
    return res_arr


def rgb_channel_values(image_path):
    image_arr = cv2.imread(image_path)
    res_arr = dict() 
    for i, color in enumerate(['r', 'g', 'b']):
        temp = cv2.calcHist([image_arr],[i],None,[256],[0,256])
        temp2 = [int(x[0]) for x in temp.tolist()]
        #temp = temp.tolist()
        res_arr[color] = temp2

    return res_arr
    
