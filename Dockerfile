# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY qr_code_generator.py /app/

# Install the required Python package
RUN pip install qrcode[pil]

# Set environment variables for customization
ENV QR_DATA_URL="https://github.com/maluis69"
ENV QR_CODE_FILENAME="github_qr.png"
ENV QR_CODE_DIR="qr_codes"
ENV FILL_COLOR="black"
ENV BACK_COLOR="white"

# Run the Python script
CMD ["python", "qr_code_generator.py"]
