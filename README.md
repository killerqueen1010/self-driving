#  Lane Detection Based on OpenCV

> A classical lane detection project based on OpenCV for autonomous driving applications.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

#  Project Overview

This project implements a classical lane detection algorithm using traditional computer vision techniques provided by OpenCV.

Unlike deep learning approaches, this project detects lane markings through image preprocessing, edge extraction and Hough Transform, making it lightweight, explainable and suitable for learning the fundamentals of autonomous driving perception.

---

#  Features

- Image preprocessing
- Grayscale conversion
- Gaussian Blur
- Canny Edge Detection
- Region of Interest (ROI)
- Hough Line Transform
- Lane visualization
- Easy to understand and extend

---

#  Project Structure

```
self-driving
│
├── README.md
├── requirements.txt
│
├── images
│   ├── road.jpg
│   └── result.png
│
└── src
    ├── lane_detection.py
    ```

---

#  Development Environment

| Item | Version |
|------|----------|
| Python | 3.10+ |
| OpenCV | 4.x |
| NumPy | Latest |
| Matplotlib | Latest |

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  How to Run

```bash
python lane_detection.py
```

The program will automatically

- Read the road image
- Detect lane boundaries
- Display the final visualization result

---

#  Algorithm Pipeline

```
Road Image
      │
      ▼
Grayscale Conversion
      │
      ▼
Gaussian Blur
      │
      ▼
Canny Edge Detection
      │
      ▼
Region of Interest
      │
      ▼
Hough Line Transform
      │
      ▼
Draw Lane Lines
      │
      ▼
Final Result
```

---

# 🔍 Core Technologies

## 1. Image Preprocessing

Convert the RGB image into grayscale and reduce noise using Gaussian filtering.

---

## 2. Edge Detection

Extract road edges using the Canny operator.

---

## 3. ROI Extraction

Keep only the lane area to reduce unnecessary interference.

---

## 4. Hough Transform

Detect straight lane lines from edge pixels.

---

## 5. Visualization

Overlay detected lane lines onto the original image.

---

#  Demonstration

## Original Image

```
images/road.jpg
```

*(Insert screenshot here after uploading.)*

---

## Detection Result

```
images/result.png
```

*(Insert screenshot here after saving your program output.)*

---

#  Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- Computer Vision

---

#  Future Improvements

- Real-time video lane detection
- Curved lane fitting
- Perspective Transformation
- Camera calibration
- ROS integration
- Deep learning based lane detection (LaneNet / SCNN / YOLOP)

---

#  Learning Objectives

This project helps beginners understand:

- Image processing fundamentals
- Feature extraction
- Edge detection
- Hough Transform
- Classical lane detection pipeline
- Autonomous driving perception

---

#  Author

**GitHub**

killerqueen1010

---

