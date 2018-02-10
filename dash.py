from PIL import Image

EPD_WIDTH = 640
EPD_HEIGHT = 384

class Dash:
    def __init__(self):
        self.image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame

    def render(self):
        return self.image
