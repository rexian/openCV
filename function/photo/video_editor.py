import cv2

cap = cv2.VideoCapture('bay_area.MOV')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('ga.MOV', fourcc, 20.0, (1920, 1080))

print(cap.isOpened())

while cap.isOpened():

    ret, frm = cap.read()

    if ret:

        out.write(frm)

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()