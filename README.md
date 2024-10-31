# real-time-object-detection-tracking
A real-time object detection and tracking system using YOLOv5 for detection and DeepSORT for tracking. This project demonstrates the ability to detect and track objects (e.g., people, vehicles) in a live video feed, showcasing skills in computer vision, real-time processing, and OpenCV.

# Real-Time Object Detection & Tracking System

![Object Detection](https://via.placeholder.com/800x400)  <!-- Replace with an appropriate image -->

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Real-Time Object Detection & Tracking System utilizes YOLO (You Only Look Once) for object detection and DeepSORT for object tracking. This project is designed to detect and track multiple objects in a live video feed, such as from a webcam or video file. 

The system can identify various objects in real time, making it suitable for applications in surveillance, autonomous vehicles, and robotics.

## Features
- Real-time object detection using YOLOv5
- Multi-object tracking with DeepSORT
- User-friendly interface for webcam feed
- Support for various video sources (webcam, video files)
- Configurable detection settings

## Technologies Used
- **Python**: The main programming language used for development.
- **OpenCV**: Library for computer vision tasks.
- **YOLOv5**: State-of-the-art object detection model.
- **DeepSORT**: A tracking algorithm for detecting and tracking objects in videos.
- **PyTorch**: Framework used for deep learning.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AyaanShaheer/real-time-object-detection-tracking.git
   cd real-time-object-detection-tracking
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv object_tracking_env
3. **Activate the virtual environment:**
   **for Windows:**
   ```bash
   object_tracking_env\Scripts\activate
   ```
   **for Mac0s/Linux**
  ```bash
  source object_tracking_env/bin/activate
```
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   
**Usage**
To run the object detection and tracking system:

1) Activate your virtual environment if you haven't already.
2) Run the main script:
   ```bash
   python main.py
3) A window will open showing the live feed from your webcam with detected objects being tracked.

   **Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

**License**
This project is licensed under the MIT License. See the LICENSE file for more information.



