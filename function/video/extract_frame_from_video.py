import cv2
import os

cam = cv2.VideoCapture("/Users/surajitpaul/PycharmProjects/vision/function/video/output/flamingo.MOV")

try:
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    ret, frame = cam.read()

    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()