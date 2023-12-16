# # Import library yang dibutuhkan
# from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

# # Buka kedua gambar menggunakan Pillow
# background_image = Image.open('D:/Wallpaper/p3r.jpg')  # Ganti 'lokasi_background_image' dengan lokasi file gambar latar belakang Anda
# overlay_image = Image.open('D:/Wallpaper/main-sp.jpg')  # Ganti 'lokasi_overlay_image' dengan lokasi file gambar yang ingin disisipkan

# # Ubah gambar background menjadi hitam-putih (grayscale), berotasi sebesar 30 derajat, dan blur
# background_image = background_image.convert("L")
# background_image = background_image.rotate(30)
# background_image = background_image.filter(ImageFilter.BLUR)

# # Ubah tingkat kecerahan gambar overlay menjadi 1.x kali lipat dan tingkat kontras menjadi 1.y kali lipat
# # Ganti 'x' dan 'y' dengan 2 digit NIM akhir Anda
# enhancer = ImageEnhance.Brightness(overlay_image)
# overlay_image = enhancer.enhance(1.9)  
# enhancer = ImageEnhance.Contrast(overlay_image)
# overlay_image = enhancer.enhance(1.5)  

# # Resize gambar overlay sesuai kebutuhan
# # overlay_image = overlay_image.resize((lebar, tinggi))  # Ganti 'lebar' dan 'tinggi' dengan ukuran yang diinginkan

# # Sisipkan gambar overlay ke dalam gambar background
# x_center = (background_image.width - overlay_image.width) // 2
# y_center = (background_image.height - overlay_image.height) // 2
# background_image.paste(overlay_image, (x_center, y_center))

# # Tambahkan teks "Informatika JOSSS!" pada gambar overlay dengan font Arial dan ukuran 24
# draw = ImageDraw.Draw(background_image)
# direktoriFont = 'C:/Windows/Fonts/Arial.ttf'  # Ganti 'lokasi_font' dengan lokasi file font Anda
# size = 24
# font = ImageFont.truetype(direktoriFont, size)
# text = "Informatika JOSSS!"
# text_width, text_height = draw.textsize(text, font)
# text_x = (background_image.width - text_width) // 2
# text_y = (background_image.height - text_height) // 2
# draw.text((text_x, text_y), text, font=font, fill='white')

# # Simpan gambar hasil edit
# background_image.save("tugas_praktikum_enam.jpg")

# # Tampilkan hasilnya
# background_image.show()


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

