# ImageOps

ImageOps is an open-source image processing API that provides a set of basic yet important functionalities to manipulate and transform images.

## Table of Contents

- [Project Overview](#project-overview)
- [Collaboration](#collaboration)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Project Overview

ImageOps aims to simplify image processing tasks by offering a straightforward API for common operations. This project was initiated to address the need for a flexible, easy-to-use image-processing solution for developers working on diverse projects. It should be noted that the API is still under development and is yet to be hosted externally.

## Collaboration

How to contribute:

1. **Fork the repository**: Start by forking the ImageOps repository to your GitHub account.
2. **Clone the repository**: clone the forked repository to your local machine
```bash
git clone https://github.com/your-username/ImageOps.git
```
3. **Create a Branch**: Create a new branch for your contribution
```bash
git checkout -b feature-or-fix-name
```
4. **Make and commit changes**: Implement your desired feature or fix in the code.
5. **Push changes: After committing the changes, push them to your forked repository
```bash
git push origin feature-or-fix-name
```
6. **Open a Pull Request**: Create a pull request from your forked repository to the main ImageOps repository.

### Testing
1. In the repository folder, create a virtual environment(optional):
```bash
python -m venv venv
```
2. Activate the environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On MacOS/Linux:
```bash
source venv/bin/activate
```
3. Install requirements:
```bash
pip install -r requirements.txt
```
The API can be tested locally by sending requests to `'http://127.0.0.1:5000/api/'`. First, the server should be started: 
```bash 
python app/main.py
```
A test image is included, with a testing code:

```bash 
python testing/testing.py
```

## Usage

ImageOps offers several endpoints for image processing tasks. here is a quick overview:

- Grayscale Conversion:
    - Endpoint: '/api/grayscale'
    - Parameters: 
        - image (`.png` -> bytes): image to be converted

- Negative Conversion:
    - Endpoint: '/api/negative'
    - Parameters: 
        - image (`.png` -> bytes): image to be converted

- Half-toning transformation:
    - Endpoint: '/api/half'
    - Parameters: 
        - image (`.png` -> bytes): image to be half-toned using Floyd Steinberg's algorithm

- Sobel Edge Detection:
    - Endpoint: '/api/sobel_edge'
    - Parameters: 
        - image (`.png` -> bytes): input image file for edge detection.

## Dependencies

ImageOps relies on the following dependencies (some might be added/deleted as the project progresses):

- Flask
- NumPy
- CV2
- Pillow

All dependencies are listed in the `requirements.txt` file.