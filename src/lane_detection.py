import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
import os

print("当前工作目录：", os.getcwd())
print("程序所在目录：", os.path.dirname(os.path.abspath(__file__)))

import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "images", "road.jpg")

print("图片路径：", IMAGE_PATH)

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("图片读取失败")
    exit()

print("图片读取成功")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height, width = img.shape[:2]

# HSV颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 黄色范围（针对图片调试）
lower_yellow = np.array([15, 60, 60])
upper_yellow = np.array([40, 255, 255])

mask = cv2.inRange(
    hsv,
    lower_yellow,
    upper_yellow
)


# 去噪

kernel = np.ones((5,5), np.uint8)

mask = cv2.morphologyEx(
    mask,
    cv2.MORPH_CLOSE,
    kernel
)

mask = cv2.morphologyEx(
    mask,
    cv2.MORPH_OPEN,
    kernel
)


# ROI区域
# 只保留道路中央区域

roi_mask = np.zeros_like(mask)

polygon = np.array([
[
    (int(width*0.25), height),
    (int(width*0.75), height),
    (int(width*0.58), int(height*0.35)),
    (int(width*0.42), int(height*0.35))
]
], dtype=np.int32)

cv2.fillPoly(roi_mask, polygon, 255)

roi = cv2.bitwise_and(mask, roi_mask)


# 边缘检测

edges = cv2.Canny(
    roi,
    50,
    150
)


# 霍夫直线检测

lines = cv2.HoughLinesP(
    edges,
    rho=1,
    theta=np.pi/180,
    threshold=50,
    minLineLength=100,
    maxLineGap=30
)


# 绘制结果

result = img_rgb.copy()

if lines is not None:

    longest_line = None
    max_len = 0

    for line in lines:

        x1, y1, x2, y2 = line[0]

        length = np.sqrt(
            (x2-x1)**2 +
            (y2-y1)**2
        )

        if length > max_len:
            max_len = length
            longest_line = (x1,y1,x2,y2)

    if longest_line is not None:

        x1,y1,x2,y2 = longest_line

        cv2.line(
            result,
            (x1,y1),
            (x2,y2),
            (255,0,0),
            6
        )


# 显示结果

plt.figure(figsize=(14,8))

plt.subplot(221)
plt.imshow(img_rgb)
plt.title("Original")

plt.subplot(222)
plt.imshow(mask,cmap='gray')
plt.title("Yellow Extraction")

plt.subplot(223)
plt.imshow(roi,cmap='gray')
plt.title("ROI")

plt.subplot(224)
plt.imshow(result)
plt.title("Lane Detection")

plt.tight_layout()
plt.show()