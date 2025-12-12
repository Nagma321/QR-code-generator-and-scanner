import cv2

detector = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)

print("Scanning... press Ctrl+C to stop.")

while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print("QR Code Data:", data)
        break

    cv2.imshow("QR Scanner", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
