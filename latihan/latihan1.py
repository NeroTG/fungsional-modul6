from PIL import Image, ImageDraw, ImageFont

def load_image(path):
    return Image.open(path)

def convert_to_bw(image):
    return image.convert("L")

def add_text(image, text, font_path='C:/Windows/Fonts/Arial.ttf', size=50, fill='yellow'):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size)
    text_width, text_height = draw.textsize(text, font)
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 2
    draw.text((text_x, text_y), text, font=font, fill=fill)
    return image

def save_image(image, path):
    image.save(path)

def show_image(image):
    image.show()

def main():
    gambarku = load_image('D:/Wallpaper/main-sp.jpg')
    gambarBW = convert_to_bw(gambarku)
    text = "Tegar Dwi 202110370311195"
    gambarBW = add_text(gambarBW, text)
    save_image(gambarBW, "percobaan_satu.jpg")
    show_image(gambarBW)

main()
