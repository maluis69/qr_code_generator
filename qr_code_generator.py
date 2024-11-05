# qr_code_generator.py
import qrcode
import os

# Retrieve URL and customization options from environment variables
url = os.getenv("QR_DATA_URL", "https://github.com/maluis69")  # Default to your GitHub URL
filename = os.getenv("QR_CODE_FILENAME", "github_qr.png")
directory = os.getenv("QR_CODE_DIR", "qr_codes")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

# Customize colors if specified
img = qr.make_image(fill_color=fill_color, back_color=back_color)
img.save(os.path.join(directory, filename))

print(f"QR code generated for {url} and saved as {filename} in {directory}")
