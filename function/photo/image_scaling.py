import cv2

try:
    image = cv2.imread('image/lego.jpg')

    (height, width) = image.shape[:2]

    res = cv2.resize(image, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    cv2.imshow('Image Edge Detection', res)
    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('lego_copy.png', res)
        cv2.destroyAllWindows()
        print('Photo saved!')

except IOError:
    print('Error while reading files !!!')