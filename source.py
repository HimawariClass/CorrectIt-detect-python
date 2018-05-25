import os
import cv2
import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))

image = cv2.imread(f'{DIR}/image/paper03.jpg')
if image is None:
  print("File not found.")
  exit()

width, height = image.shape[:2]

# ret, image = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY) # use threshold
extracted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:, :, 1]
ret, thrshld_ex = cv2.threshold(extracted, 20, 255, cv2.THRESH_BINARY_INV)

# im_cont, contours, hierarchy = cv2.findContours(thrshld_ex, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# print(len(contours))
#
# contours_drawed = image.copy()
#
# for conts in contours:
#   contours_drawed = cv2.drawContours(contours_drawed, contours, 3, (0, 255, 0))

mask = np.zeros((width+2, height+2), np.uint8)
mask[:] = 0
cv2.floodFill(thrshld_ex, mask, (0, 0), (0, 0, 255))

cv2.imwrite(f'{DIR}/image/out.png', thrshld_ex)
