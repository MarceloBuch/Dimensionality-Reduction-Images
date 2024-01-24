from PIL import Image
import os

def rgb_to_gray(pixel):
    return sum(pixel) // 3

def color_to_gray(input_image, output_image):
    original_image =  Image.open(input_image)

    width, height = original_image.size

    gray_image = Image.new("L", (width, height))

    for x in range(width):
        for y in range(height):
            pixel = original_image.getpixel((x, y))
            gray_value = rgb_to_gray(pixel)
            gray_image.putpixel((x, y), gray_value)

    output_path = os.path.join(output_image, "tons_de_cinza.jpg")
    gray_image.save(output_path)

def gray_to_bw(input_image, output_image, threshold = 30):
    gray_image = Image.open(input_image)
    bw_image = gray_image.point(lambda x: 0 if x < threshold else 255, '1')
    output_path = os.path.join(output_image, "preto_e_branco.jpg")
    bw_image.save(output_path)


input_image_path = "./img/input/WhatsApp Image 2023-12-26 at 16.01.49.jpeg"
output_image = "./img/output/"

color_to_gray(input_image_path, output_image)
gray_to_bw(os.path.join(output_image, "tons_de_cinza.jpg"), output_image)