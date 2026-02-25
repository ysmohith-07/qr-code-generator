import qrcode

def create_qr_code(url, filename="website_qr.png"):
    """
    Generates a QR code from a given URL and saves it as an image.
    """
    # 1. Configure the QR code settings
    qr = qrcode.QRCode(
        version=1,                                     # Size of the QR Code (1 is the smallest, up to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction (good if you want to add logos later)
        box_size=10,                                   # Size of each tiny square in pixels
        border=4,                                      # Thickness of the white border (minimum is usually 4)
    )

    # 2. Add the website data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # 3. Create the image (you can change the colors here!)
    img = qr.make_image(fill_color="black", back_color="white")

    # 4. Save the image to your computer
    img.save(filename)
    print(f"Success! Your QR code has been saved as: {filename}")

# --- Run the Script ---
if __name__ == "__main__":
    # Ask the user to input a website URL
    user_url = input("Enter the website URL you want to convert: ")

    # Generate it!
    create_qr_code(user_url)