import qrcode as qr
from PIL import Image
qr1=qr.QRCode(version=1,
            border=10,box_size=10)
qr1.add_data("https://www.geeksforgeeks.org/netstat-command-linux/")
qr1.make(fit=True)
img =qr1.make_image(fill_color="green",back_color="white")
img.save("image.png")