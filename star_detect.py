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
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('stasImage',img);
# accessing pixels
print img[20,20]
_, threshold =  cv2.threshold(img, 127, 255, cv2.THRESH_BINARY, dst=None);
_, threshold2 =  cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY, dst=None);
cv2.imshow('threshold', threshold);
cv2.imshow('threshold2', threshold2);
cv2.waitKey(0);
cv2.destroyAllWindows();
