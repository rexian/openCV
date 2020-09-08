import cv2

image = cv2.imread('image/lego.jpg')

window_name = 'Image'

image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

cv2.imshow(window_name, image)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lego_copy.png', image)
    cv2.destroyAllWindows()
    print('Photo saved!')