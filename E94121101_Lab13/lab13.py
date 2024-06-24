import cv2
import numpy as np

image = cv2.imread("TW.jpg") # read image
B,G,R = cv2.split(image) # split BGR channel
zeros = np.zeros(image.shape[:2],dtype="uint8") # create 0 Matrix
grayFunc = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # turn BGR into gray (Using Function)
grayNoFunc = (B+G+R)//3 # turn BGR into gray (Not Using Function)
# using '//' to make every element be an integer
ret, binaryImage = cv2.threshold(grayFunc, 245, 255, cv2.cv2.THRESH_BINARY)
# using cv2.threshold(image, thresh, maxval, type) to binarize the gray image

# show 4 images
cv2.imshow("Origin", image)
cv2.imshow("UsingFunction", grayFunc)
cv2.imshow("NoUsingFunction", grayNoFunc)
cv2.imshow("BinaryImage", binaryImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

# save 4 images
cv2.imwrite("Origin.jpg", image)
cv2.imwrite("UsingFunction.jpg", grayFunc)
cv2.imwrite("NoUsingFunction.jpg", grayNoFunc)
cv2.imwrite("BinaryImage.jpg", binaryImage)