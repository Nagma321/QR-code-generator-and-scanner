import qrcode

data = input("Enter text or URL for QR Code: ")

qr = qrcode.make(data)
qr.save("my_qr.png")

print("QR Code generated successfully ➜ my_qr.png")
