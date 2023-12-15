from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog, Tk


def get_image_files():
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfiles(initialdir="/Users/joshmaitre/Desktop", title='Select Image(s)')
    return files


def add_watermark(image_path, wm_text='@JoshMaitre'):
    opened_image = Image.open(image_path)
    width, height = opened_image.size

    font_size = int(width / 50)
    font = ImageFont.truetype('Arial.ttf', font_size)

    x, y = int(width * 0.90), int(height * 0.95)

    draw = ImageDraw.Draw(opened_image)
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    opened_image.show()
    opened_image.save(image_path)


def main():
    files = get_image_files()
    for file in files:
        add_watermark(file.name)


if __name__ == "__main__":
    main()
