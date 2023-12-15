import os

from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.withdraw()
file_as_str = filedialog.askopenfiles(initialdir="/Users/joshmaitre/Desktop", title='Select Image(s)')


def add_watermark(image, wm_text):
    opened_image = Image.open(image)

    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font_size = int(image_width / 50)  # Aspect ratio for text size

    font = ImageFont.truetype('Arial.ttf', font_size)

    # Coordinates for where we want the image
    x, y = int(image_width * .90), int(image_height * .95)

    # Add the watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    # Show Image
    opened_image.show()

    # Save Image
    opened_image.save(file_path)


for file in file_as_str:
    file_path = file.name
    add_watermark(file_path, 'HACKED')
    print(file.name)
