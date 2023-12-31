from flask import Blueprint, request, jsonify, Response
from image_processing import *
import os
from dotenv import load_dotenv

load_dotenv()

api_bp = Blueprint('api', __name__)

valid_api_key = os.environ.get('API_KEY')


def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key == valid_api_key:
            return func(*args, **kwargs)
        else:
            return jsonify({'error': 'Invalid API key'}), 401
    wrapper.__name__ = func.__name__
    return wrapper


@api_bp.route('/')
def home():
    return 'Welcome to the ImageOps API: Please see documentation for example use'


@api_bp.route('/grayscale', methods=['POST'])
@require_api_key
def convert_to_grayscale_route():
    try:
        file = request.files['image']
        bytes = file.read()

        grayscale_image_bytes = convert_to_grayscale(bytes)

        return jsonify({'grayscale_image': grayscale_image_bytes.hex()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


@api_bp.route('/resize', methods=['POST'])
@require_api_key
def resize_image_route():
    try:
        file = request.files['image']
        bytes = file.read()

        width = int(request.form['width'])
        height = int(request.form['height'])

        resized_image = resize_image(bytes, (width, height))

        return jsonify({'resize_image': resized_image.hex()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e) + ',\n Message from backend: ' + resized_image}), 500

@api_bp.route('/negative', methods=['POST'])
@require_api_key
def convert_to_neg_route():
    try:
        file = request.files['image']
        bytes = file.read()

        negative = convert_to_negative(bytes)

        # Return a JSON response with the hex-encoded negative image
        return jsonify({'negative_image': negative.hex()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/half', methods=['POST'])
@require_api_key
def half_tone_route():
    try:
        file = request.files['image']
        bytes = file.read()

        half_toned = half_tone(bytes)

        return jsonify({'half_image': half_toned.hex()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/sobel_edge', methods=['POST'])
@require_api_key
def sobel_route():
    try:
        file = request.files['image']
        bytes = file.read()

        sobel_edge = sobel_edge_detection(bytes)

        return jsonify({'sobel_edge_image': sobel_edge.hex()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



