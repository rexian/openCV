import cv2

image = cv2.imread('image/lego.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lego_copy.png', gray_image)
    cv2.destroyAllWindows()
    print('Photo saved!')