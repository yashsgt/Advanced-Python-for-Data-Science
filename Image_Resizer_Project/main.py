import cv2

image = cv2.imread(r"C:\Users\Yash\PycharmProjects\Image-resizer\393735.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)

# Percent by which image is resized
scale_percent = 50

# calculate the 50 percent of original dimensions
new_width = int(image.shape[1]*scale_percent/100)
new_height = int(image.shape[0]*scale_percent/100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(image, dsize)

cv2.imwrite('newImage.png', output)
cv2.waitKey(0)