from pathlib import Path
from PIL import Image, ImageDraw
import numpy
import base64
from io import BytesIO

# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()



def image_data(path=Path("static/assets/images/"), img_list=None):  # path of static images is defaulted

    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)

# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)



# color_data prepares a series of images for data analysis
def image_data(path=Path("static/assets/images/"), img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Car 2", 'label': "Car 2", 'file': "Model S.jpeg"},
            {'source': "Car 3", 'label': "Car 3", 'file': "Taycan.jpeg"},
            {'source': "Car", 'label': "Car", 'file': "2021.jpeg"},
            {'source': "Horse", 'label': "Funny Horse", 'file': "funnyhorse.jpg"},
            {'source': "Horse", 'label': "Funny Horse", 'file': "funnyanimal.jpg"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # img_dict['path'] = '/' + path  # path for HTML access (frontend)
        #file = path + img_dict['file']  # file with path for local access (backend)
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # Start of pillow test code
        img = Image.open(file)
        #erase previous drawing on image
        d1 = ImageDraw.Draw(img)
        d1.text((28, 36), "Hello, Text above Images!", fill=(255, 0, 0))
        # img.show()

        # End of pillow test code

        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary