# QR Code Scanner
import cv2 # For reading the QR code
import webbrowser
import pyqrcode # For creating the qr code
import png # For exporting png files
from pyqrcode import QRCode
import datetime # For the date of when the QR code was read
from datetime import date
import os

possibleInputs = ["Scan", "SCAN", "scan", "Make", "MAKE", "make"] 
today = date.today()
e = datetime.datetime.now()

while 1:
    start = str(input("Do you want to SCAN or MAKE QR code? (SCAN/MAKE):"))
    if start in possibleInputs:
        break
    else:
        print("enter SCAN or MAKE")
if start in ["make","Make","MAKE"]:
    content = input("Insert content for the QR code:")
    url = pyqrcode.create(content)
    fileName = str(input("What do you want to name the file?: "))
    url.png(fileName + ".png",scale=6)
else:
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _,img = cap.read()  
        data,one, _ = detector.detectAndDecode(img)
        if data:
            a = data
            break
        cv2.imshow("qrcodescanner app", img)
        if cv2.waitKey(1)==ord("q"): # If you want to close the scanner, press "q"
            break
    b = webbrowser.open(str(a))
    txtFileName = (str(today)+".txt")
    check = os.path.exists(txtFileName)
    if check is True:
        textFile = open(txtFileName, "a")
        n = textFile.write("\n" + "\n" + "Data:" + "\n" + str(a) + "\n" + "Date scanned:" + "\n" + str(e))
    else:
        textFile = open(txtFileName, "w")
        n = textFile.write("Data:" + "\n" + str(a) + "\n" + "Date scanned:" + "\n" + str(e))
        textFile.close()
    cv2.destroyAllWindows
    