import cv2 as cv

a = input("Enter the name of the image: ")
img_path = f"images/{a}.jpg"

# img = cv.imread('images/animal.jpg')

cv.imshow('cat',img_path)

cv.waitKey(0)