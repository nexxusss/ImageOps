"""
Program to send request to the image processing API

Actions:
    - grayscale: convert the payload image to grayscale
    - resize: resize the image
    - negative: generate negative of the image
    - half: Half-toning using Floyd and Steinberg algorithm
    - sobel_edge: Edge detection using Sobel filters
"""

import requests
import os
import binascii
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')
ROOT = 'http://127.0.0.1:8000/api/'

image_path = 'testing/resources/woman.png'


def send_request(action: str, params: dict, image_path: str) -> None:
    r"""
    Example function to send request to the API with payload image

    params:
        action (str): action to perform
        image_path (str): path to the input image

    return:
        None, function saves the input image locally
    """

    url = ROOT + action
    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        exit()

    # Prepare the image file
    files = {'image': (os.path.basename(image_path), open(image_path, 'rb'))}

    
    # Send the POST request
    response = requests.post(url, files=files, data=params, headers={'X-API-Key': str(api_key)})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the hex-encoded bytes from the JSON response
        hex_bytes = response.json().get(f'{action}_image')

        # Convert hex to bytes
        resized_image_bytes = binascii.unhexlify(hex_bytes)

        # Save the resized image locally as 'resized_image.png'
        with open(f'{action}.png', 'wb') as f:
            f.write(resized_image_bytes)
        print(f"{action} image saved as '{action}.png'")
    else:
        print(f"[LOGS]: Error in the POST request: {response.reason}")
        print(f"[LOGS]: Error message from server: {response.json().get('error')}")


action = 'resize'
#passing arguments for functions
# if calling resize then we can pass the following
params = {'width': 600, 'height': 400}

send_request(action, params, image_path)

