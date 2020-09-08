import cv2

try:
    image = cv2.imread('image/lego.jpg')

    (rows, cols) = image.shape[:2]

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(image, M, (cols, rows))

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