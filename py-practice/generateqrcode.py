import qrcode
import image
import time

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=10
)

link = input("link: ")
img_name = input('Image name: ')



# seconds = time.time()

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save(f"{img_name}.png")