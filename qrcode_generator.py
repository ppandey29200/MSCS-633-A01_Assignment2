import qrcode
from PIL import Image, ImageTk
import tkinter as tk

def generate_qr_code(url, filename="biox_qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

def display_qr_code(image_path):
    root = tk.Tk()
    root.title("img")

    # Load image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Display image in Label
    label = tk.Label(root, image=photo)
    label.image = photo  # keep a reference!
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    url = "https://www.bioxsystems.com/"
    qr_image_path = generate_qr_code(url)
    display_qr_code(qr_image_path)