import numpy as np
import cv2
from PIL import Image
import io

def resize_image(bytes, size=(300, 300)):
    """
    Resize an image given new dimension
    params:
        bytes: bytes of the input image
        size: target resizing dimensions
    return:
        resized image
    """
    try:
        image = Image.open(io.BytesIO(bytes))
        resized_image = image.resize(size)
        
        img_byte_array = io.BytesIO()
        resized_image.save(img_byte_array, format='PNG')
        return img_byte_array.getvalue()

    except Exception as e:
        return str(e)
    
def convert_to_grayscale(bytes):
    """
    Convert a color image to grayscale image
    params:
        bytes: bytes of the input image
    return:
        Grayscale image
    """
    try:
        image = Image.open(io.BytesIO(bytes))

        # Check if there are 3 channels / is color image
        if len(np.array(image).shape) == 3 and np.array(image).shape[2] == 3:
            grayscale_image = image.convert('L')
            
            img_byte_array = io.BytesIO()
            grayscale_image.save(img_byte_array, format='PNG')
            return img_byte_array.getvalue()
        else:
            return "Image is already in grayscale."

    except Exception as e:
        return str(e)
    
def convert_to_negative(image_bytes):
    """
    Generate the negative version of an image using cv2
    
    Params:
        image_bytes: Bytes of the input image
    
    Return:
        Negative image as bytes
    """
    try:
        # Convert the image bytes to a NumPy array
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)

        # Decode the array to an OpenCV image
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # Generate the negative image
        negative_image = 255 - image

        # Encode the negative image to bytes
        _, negative_image_bytes = cv2.imencode('.png', negative_image)

        return negative_image_bytes.tobytes()

    except Exception as e:
        return str(e)
