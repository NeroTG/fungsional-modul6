
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def load_image(path):
    return Image.open(path)

def convert_to_grayscale(image):
    return image.convert("L")

def rotate_image(image, degrees):
    return image.rotate(degrees)

def blur_image(image):
    return image.filter(ImageFilter.BLUR)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def calculate_center(background_image, overlay_image):
    x_center = (background_image.width - overlay_image.width) // 2
    y_center = (background_image.height - overlay_image.height) // 2
    return x_center, y_center

def paste_image(background_image, overlay_image, coordinates):
    background_image.paste(overlay_image, coordinates)
    return background_image

def add_text(image, text, font_path='C:/Windows/Fonts/Arial.ttf', size=24, fill='white'):
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
    background_image = load_image('D:/TG/Kuliah/Semester5/PemrogramanFungsional/background.jpg')
    overlay_image = load_image('D:/TG/Kuliah/Semester5/PemrogramanFungsional/umm.jpg')
    background_image = convert_to_grayscale(background_image)
    background_image = rotate_image(background_image, 30)
    background_image = blur_image(background_image)
    overlay_image = adjust_brightness(overlay_image, 1.9)
    overlay_image = adjust_contrast(overlay_image, 1.5)
    coordinates = calculate_center(background_image, overlay_image)
    background_image = paste_image(background_image, overlay_image, coordinates)
    background_image = add_text(background_image, "Informatika JOSSS!")
    save_image(background_image, "tugas_praktikum_enam.jpg")
    show_image(background_image)

main()

