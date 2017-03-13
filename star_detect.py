# from PIL import Image;
# import cv2;
# star_image = Image.open("star_hubble.jpg");
# pixels = star_image.load();
# print star_image.size
# print(pixels[22,22]);
# # # star_image.show()
# # star_image.show();
# c = raw_input();

import cv2;
import numpy as np;
# Loading image and showing on screen
img = cv2.imread('star_hubble.jpg');
# Loading template for star
template  = cv2.imread('template.jpg',0);
#changing into gray scale
w,h = template.shape[::-1]
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
threh = 0.4
loc = np.where(result>=threh)
for pt in zip(*loc[::-1]):
    #
    # cv2.rectangle(img, pt, (pt[0]+w),(pt[1]+h), (0,255,255),2)
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h),(0,255,255),1)
cv2.imshow('stasImage',img);
cv2.imwrite('detected.jpg', img, params=None)
# accessing pixels
# print img[20,20]
_, threshold =  cv2.threshold(img, 127, 255, cv2.THRESH_BINARY, dst=None);
_, threshold2 =  cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY, dst=None);
# cv2.imshow('threshold', threshold);
# cv2.imshow('threshold2', threshold2);

cv2.waitKey(0);
cv2.destroyAllWindows();
