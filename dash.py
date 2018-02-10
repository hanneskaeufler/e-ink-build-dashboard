from PIL import Image
from PIL import ImageDraw


class Dash:
    WIDTH = 640
    HEIGHT = 384

    def __init__(self):
        self.image = self.__clear_image()
        self.draw = ImageDraw.Draw(self.image)

    def render(self):
        self.draw.rectangle((0, 0, 10, 10), fill = 0)

        return self.image

    def __clear_image(self):
        return Image.new('1', (self.WIDTH, self.HEIGHT), 1)    # 1: clear the frame

