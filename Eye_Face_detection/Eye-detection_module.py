 
import cv2

Video = cv2.VideoCapture(0)


while True:
    success, img = Video.read()
    

        # showing the webcam video

    cv2.imshow("WebCam", img)

        # important line to break the webcam terminal after pressing any key

    if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # For closing the terminal after use

Video.release()
cv2.destroyAllWindows()
