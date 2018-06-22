import os
import cv2
import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))

image = cv2.imread(f'{DIR}/image/paper02.jpg')
if image is None:
  print("File not found.")
  exit()

width, height = image.shape[:2]

# ret, image = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY) # use threshold
extracted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:, :, 1]
ret, thrshld_ex = cv2.threshold(extracted, 50, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 1), np.uint8)
thrshld_ex = cv2.morphologyEx(thrshld_ex, cv2.MORPH_OPEN, kernel)

im_cont, contours, hierarchy = cv2.findContours(thrshld_ex, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print(len(contours))

print(hierarchy)

contours_drawed = image.copy()

# cv2.drawContours(contours_drawed, contours, 10, (0, 0, 255))

for index in range(len(contours)):
  cv2.drawContours(contours_drawed, contours, index, (0, 0, 255), 1)
  # index += 1

# mask = np.zeros((width+2, height+2), np.uint8)
# mask[:] = 0
# cv2.floodFill(thrshld_ex, mask, (0, 0), (0, 0, 255))

cv2.imwrite(f'{DIR}/image/out.png', thrshld_ex)
cv2.imwrite(f'{DIR}/image/out_contours.png', contours_drawed)
