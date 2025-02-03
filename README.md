# Color Detection using OpenCV, Pillow, and NumPy
This project demonstrates color detection in real-time using a webcam, implemented in Python with the OpenCV, Pillow, and NumPy libraries. The program detects a specified color (yellow in this case) in the live video feed, draws a bounding box around the detected color, and displays the result.

# Features
Real-time color detection using a webcam feed.

Bounding box drawn around detected color regions.

Customizable color detection through the get_limits function.

Uses OpenCV for image processing and real-time video capture.

Pillow for image manipulation and bounding box calculation.

# Setup & Installation
Clone this repository to your local machine:
<blockquote>
git clone https://github.com/yourusername/color-detection.git
</blockquote>

Install the required dependencies:
<blockquote>
pip install opencv-python pillow numpy
</blockquote>  
Run the main script (main.py) to start the color detection:
<blockquote>
python main.py
</blockquote>
Press 'q' to exit the webcam window.

# How it Works
The program captures video from your webcam using OpenCV.
It converts the captured frames to the HSV color space for easier color detection.
The get_limits function defines the color range (yellow in this case) and creates a mask to isolate the color.
A bounding box is drawn around detected regions of the specified color, and the result is displayed.
Customization
Modify the yellow variable in main.py to detect different colors. The get_limits function automatically adjusts the HSV range for the new color.
You can also tweak the lower and upper HSV limits inside the get_limits function for more precise color detection.
# Requirements
Python 3.x

OpenCV

Pillow

NumPy
