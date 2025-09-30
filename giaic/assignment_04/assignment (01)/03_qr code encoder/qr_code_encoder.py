import qrcode  # Import the qrcode module

data = 'Data to encode in QR code'

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)

qr.add_data(data)
qr.make(fit=True)

# Generate and save the first QR code with green color
img = qr.make_image(fill_color='green', back_color='white')
img.save("C:/Users/qasim/OneDrive/Desktop/Python_Projects/assignment (01)/qr code encoder/qr_image1.png")

# Simpler method to generate QR code (without manual configuration)
img2 = qrcode.make(data)  # Using the module reference
img2.save("C:/Users/qasim/OneDrive/Desktop/Python_Projects/assignment (01)/qr code encoder/qr_image2.png")
