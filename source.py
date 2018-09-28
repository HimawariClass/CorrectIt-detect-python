import os
import cv2
import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))

 image = cv2.imread(f'{DIR}/image/paper03.jpg')
if image is None:
  print("File not found.")
  exit()

def write_out(img, name):
  cv2.imwrite(f'{DIR}/image/result/{name}.png', img)

def extract_inside(contours, hierarchy, debug=False):
  extracted = []
  contours_drawed = image.copy()
  if debug:
    print(f'len: {len(contours)}')
    print(hierarchy)

  for index in range(len(contours)):
    if hierarchy[0][index][2] != -1 or cv2.contourArea(contours[index]) < 8000:
      continue

    extracted.append(contours[index])
    
    if debug:
      cv2.drawContours(contours_drawed, contours, index, (255, 0, 255), 1)

    print(f'{index} : {cv2.contourArea(contours[index])}')
  
  if debug:
    write_out(contours_drawed, 'out_contours')
  
  return extracted

width, height = image.shape[:2]

# ret, image = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY) # use threshold
extracted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:, :, 1]
ret, thrshld_ex = cv2.threshold(extracted, 50, 255, cv2.THRESH_BINARY)

write_out(thrshld_ex, 'thrshld')

kernel = np.ones((3, 1), np.uint8)
thrshld_ex = cv2.morphologyEx(thrshld_ex, cv2.MORPH_OPEN, kernel)

_, contours, _ = cv2.findContours(thrshld_ex, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

inside_contours = extract_inside(contours, hierarchy, True)

write_out(thrshld_ex, 'out')

