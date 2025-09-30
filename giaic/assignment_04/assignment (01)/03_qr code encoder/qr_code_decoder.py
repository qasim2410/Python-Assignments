from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/qasim/OneDrive/Desktop/Python_Projects/assignment (01)/qr code encoder/qr image.png")

results = decode(img)

print(results)  # ✅ Fixed: Removed `.Solve`
