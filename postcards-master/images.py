from PIL import Image, ImageDraw, ImageFont, ImageColor
from random import randint, choice
from os import listdir
from imageio.v3 import imread

def add_text(image: Image, text: str, font: ImageFont, x, y, color):
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text, fill=color, font=font)

def add_image(image1: Image, image2: Image, x, y):
    back_im = image1.copy()
    back_im.paste(image2, (x, y))
    return back_im

def get_random_background():
    back = choice(listdir("back"))

    img = Image.open(f"back/{back}")

    return img

def get_random_animal():
    animal = choice(listdir("animals"))

    img = Image.fromarray(imread(uri=f"animals/{animal}"))

    return img

def get_random_font(size):
    font_path = choice(listdir("fonts"))

    font = ImageFont.truetype(f"fonts/{font_path}", size)

    return font

def get_random_gif():
    gif = choice(listdir("gifs"))

    img = Image.open(f"gifs/{gif}")

    return img


def get_random_color():
    return (100+randint(0,50), 0+randint(0,50), 100+randint(0,50))