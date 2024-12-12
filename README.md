# Face Detection with OpenCV

This project demonstrates a basic implementation of face detection using OpenCV in Python. A pre-trained Haar Cascade classifier is used to detect faces in real-time from a webcam feed. Detected faces are highlighted with rectangles in the video stream.

## Features
- Real-time face detection using a webcam.
- Highlights detected faces with rectangles.
- Easy-to-understand implementation with minimal dependencies.

## Requirements

Before running the project, ensure you have the following:

- Python 3.x
- OpenCV library
- A webcam connected to your computer

## Installation

1. Clone this repository or copy the code into a new project directory:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required library:

    ```bash
    pip install opencv-python
    ```

## Usage

1. Save the provided code to a Python file, for example, `face_detection.py`.

2. Run the script:

    ```bash
    python face_detection.py
    ```

3. The webcam feed will open in a new window. Detected faces will be outlined with rectangles.

4. Press the 'q' key to exit the application.