from images import get_random_background, get_random_animal, add_text, add_image, get_random_font, get_random_color, get_random_gif
from random import randint
from text_generator import generate_text
from PIL import ImageFont

def get_animal(back):
    animal = get_random_animal()
    while animal.width >= back.width//2 or animal.height >= back.height//2:
        w, h = animal.size
        animal = animal.resize((w//2, h//2))
    return animal

def get_gif(back):
    gif = get_random_gif()
    while gif.width >= back.width//2 or gif.height >= back.height//2:
        w, h = gif.size
        gif = gif.resize((w//2, h//2))
    return gif

class Postcard:
    def __init__(self):
        self._back = get_random_background()
        self._animals = [get_animal(self._back) for i in range(randint(1, 2))]
        self._gifs = [get_gif(self._back) for i in range(randint(1, 4))]
        self._text = generate_text()
        self._font = get_random_font(self._back.width//len(self._text))
        self._font_color = get_random_color()

        self.result = self._back

    def draw(self):
        text_y = randint(0, self._back.height - self._font.size)
        text_y2 = randint(0, self._back.height)
        result = self.result
        for animal in self._animals:
            result = add_image(result if result is not None else self._back, animal, randint(0, self._back.width), randint(0, self._back.height))
        for gif in self._gifs:
            result = add_image(result if result is not None else self._back, gif, randint(0, self._back.width), randint(0, self._back.height))
        add_text(result, self._text, self._font, 0, text_y, self._font_color)
        if randint(0, 100) > 34:
            add_text(result, "Автор: FOTO-PRIKOL.NET", get_random_font(randint(10, 14)), 0, text_y2, self._font_color)

        return result

    def save(self, result, path):
        result.save(path)

    def draw_and_save(self, path):
        self.save(self.draw(), path)
