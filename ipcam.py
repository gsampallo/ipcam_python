import cv2
cap = cv2.VideoCapture('URL')
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('img.png',gray)
cap.release()