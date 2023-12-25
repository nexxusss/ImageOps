import numpy as np
import cv2
from PIL import Image
import io

T = 127

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


def find_closest_palette_color(oldpixel):
    # Implementation of finding the closest palette color
    # This function depends on some specific requirements
    # It could involve simple rounding or more advanced color matching algorithms
    # For the sake testing we will use simple rounding
    return np.round(oldpixel / 255) * 255


def half_tone(image_bytes):
    """
    Apply half-toning of an image using FLoyd-Steinbergs algorithm
    Image should be grayscale

    Params:
        image_bytes: Bytes of the input image
    
    Return:
        Negative image as bytes
    """
    # some threshold set by testing
    threshold = T

    try:
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        # Decode the array to an OpenCV image
        in_image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

        image = np.copy(in_image).astype(float)
        height = image.shape[0]
        width = image.shape[1]

        for y in range(height - 1):
            for x in range(width - 1):
                oldpixel = image[y][x]
                newpixel = find_closest_palette_color(oldpixel)
                # newpixel = 255 if oldpixel > 127 else 0
                image[y][x] = newpixel
                error = oldpixel - newpixel

                image[y][x + 1] = image[y][x + 1] + error * 7 / 16
                image[y + 1][x - 1] = image[y + 1][x - 1] + error * 3 / 16
                image[y + 1][x] = image[y + 1][x] + error * 5 / 16
                image[y + 1][x + 1] = image[y + 1][x + 1] + error * 1 / 16

        # Encode the negative image to bytes
        _, half_toned = cv2.imencode('.png', image)

        return half_toned.tobytes()

    except Exception as e:
        return str(e)
    

def sobel_edge_detection(image_bytes):
    """
    Perfrom edge detection using Sobel filters
    Image should be grayscale, else direcly converted to grayscale

    Params:
        image_bytes: Bytes of the input image
    
    Return:
        Negative image as bytes
    """
    try:
        # Convert image bytes to NumPy array
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        
        # Decode the array to an OpenCV image in grayscale
        image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

        # Apply Sobel edge detection
        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

        # Combine the results
        magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
        magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

        # Encode the result to bytes
        _, edge_detected_image = cv2.imencode('.png', magnitude)

        return edge_detected_image.tobytes()

    except Exception as e:
        return str(e)

