import cv2

image = cv2.imread('image/lego.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

edges = cv2.Canny(image, 100, 200)

cv2.imshow('Image Edge Detection', edges)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lego_copy.png', edges)
    cv2.destroyAllWindows()
    print('Photo saved!')