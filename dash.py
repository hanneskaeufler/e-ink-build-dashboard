from PIL import Image
from PIL import ImageDraw

EPD_WIDTH = 640
EPD_HEIGHT = 384

class Dash:
    def __init__(self):
        self.image = self.__clear_image()
        self.draw = ImageDraw.Draw(self.image)

    def render(self):
        self.draw.rectangle((0, 0, 10, 10), fill = 0)

        return self.image

    def __clear_image(self):
        return Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame

