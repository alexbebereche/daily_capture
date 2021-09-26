import cv2
import os
from datetime import date

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

PATH = f"E:\\projects\\ss\\screenshots"

today = date.today()

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        # img_name = "E:\projects\opencv_frame_{}.png".format(img_counter)
        # cv2.imwrite(img_name, frame)
        # print("{} written!".format(img_name))
        # img_counter += 1
        # d1 = today.strftime("%d/%m/%Y")
        day = str(date.today().strftime("%d_%m_%Y"))
        cv2.imwrite(os.path.join(PATH , day + ".jpg"), frame)
        print("took a screenshot")

cam.release()

cv2.destroyAllWindows()