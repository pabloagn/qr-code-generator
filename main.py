import qrcode
from PIL import Image
import os

# Define paths
vcard_file_path = './data/vcard-1.txt'
assets_dir = "assets"
logo_path = os.path.join(assets_dir, 'Solenoid Labs - Icon - Black Solid.png')
output_file_path = os.path.join(assets_dir, "vcard_qr_code_with_logo.png")

# Read vCard data from file
with open(vcard_file_path, 'r') as file:
    vcard_data = file.read()

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo image
logo = Image.open(logo_path)

# Calculate the size of the logo
box_size = img.size[0] // qr.box_size
logo_size = box_size * 3
logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

# Calculate the position to place the logo
logo_position = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

# Paste the logo into the QR code
img.paste(logo, logo_position, mask=logo)

# Save the QR code with the logo
img.save(output_file_path)

print(f"QR Code generated and saved as '{output_file_path}'")
