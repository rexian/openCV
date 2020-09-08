import cv2

img1 = cv2.imread('image/shylin.jpg', 1)
img2 = cv2.imread('image/lego.jpg', 1)

weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('Weighted Image', weightedSum)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()