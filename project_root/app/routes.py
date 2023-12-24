from flask import Blueprint, request, jsonify, Response
from image_processing import *

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return 'Welcome to the IMG-PRO API'


@api_bp.route('/grayscale', methods=['POST'])
def convert_to_grayscale_route():
    try:
        file = request.files['image']
        bytes = file.read()

        grayscale_image_bytes = convert_to_grayscale(bytes)

        return jsonify({'grayscale_image': grayscale_image_bytes.hex()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


@api_bp.route('/resize', methods=['POST'])
def resize_image_route():
    try:
        file = request.files['image']
        bytes = file.read()

        resized_image = resize_image(bytes)

        return jsonify({'resize_image': resized_image.hex()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/negative', methods=['POST'])
def convert_to_neg_route():
    try:
        file = request.files['image']
        bytes = file.read()

        negative = convert_to_negative(bytes)

        # Return a JSON response with the hex-encoded negative image
        return jsonify({'negative_image': negative.hex()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


