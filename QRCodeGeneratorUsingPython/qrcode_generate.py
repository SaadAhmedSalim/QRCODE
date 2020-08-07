import qrcode   # pip3 install qrcode
from pyzbar.pyzbar import decode    # pip3 install pyzbar
from PIL import Image  # pip3 install pillow

""" Frame of QR Code"""

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
    )

data1 = "QR Code"
qr.add_data(data1)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save("/home/saad/Documents/QRCodeGeneratorUsingPython/QR.png")


""" QR Code Reader"""
qr_reader = decode(Image.open("/home/saad/Documents/QRCodeGeneratorUsingPython/1.png"))

# decode will show the info of the qrcode pictures file
# As I downloaded 1.png from Internet and its description is Hello :)
print(qr_reader[0].data.decode())
