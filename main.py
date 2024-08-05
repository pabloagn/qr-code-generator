import qrcode
from PIL import Image

# Define the vCard data
vcard_data = """
BEGIN:VCARD
VERSION:3.0
FN:John Doe
ORG:Company
TEL:+1-234-567-890
EMAIL:john.doe@example.com
END:VCARD
"""

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
logo = Image.open('/mnt/data/qr-code-1.png')

# Calculate the size of the logo
box_size = img.size[0] // qr.box_size
logo_size = box_size * 3
logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

# Calculate the position to place the logo
logo_position = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

# Paste the logo into the QR code
img.paste(logo, logo_position, mask=logo)

# Save the QR code with the logo
img.save("vcard_qr_code_with_logo.png")

print("QR Code generated and saved as 'vcard_qr_code_with_logo.png'")
