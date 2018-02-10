from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime

class Dash:
    WIDTH = 640
    HEIGHT = 384

    BLACK = 0
    WHITE = 255

    PROJECTS = ('PitBuddy iOS', 'PitBuddy Android', 'Blog', 'danger-todoist', 'danger-plugin-mentor')

    def __init__(self):
        self.image = self.__clear_image()
        self.draw = ImageDraw.Draw(self.image)
        self.title_font = ImageFont.truetype('FreeMonoBold.ttf', 32)
        self.font = ImageFont.truetype('Lato-Regular.ttf', 32)

    def render(self):
        self.__render_header()
        self.__render_rows()

        return self.image

    def __render_header(self):
        self.draw.rectangle((0, 0, 10, 10), fill = self.BLACK)
        self.draw.rectangle(self.__header_rect_pos(), fill = self.BLACK)
        # TODO: Automatical vertical and horizontal centering?
        self.draw.text((self.__from_left(160), self.__from_top(17)),
                       self.__title(),
                       font = self.title_font,
                       fill = self.WHITE)

    def __render_rows(self):
        padding = 10
        guessed_font_vertical_padding = 13

        for index, project in enumerate(self.PROJECTS):
            self.draw.text((self.__from_left(padding), (index + 1) * self.__row_height() + guessed_font_vertical_padding), project, font = self.font, fill = self.BLACK)

    def __title(self):
        return datetime.date.today().strftime('%B %d, %Y')

    def __header_rect_pos(self):
        return (self.__left(),
                self.__top(),
                self.__right(),
                self.__from_top(1 * self.__row_height()))

    def __row_height(self):
        return self.HEIGHT / 6

    def __right(self):
        return self.__from_right(0)

    def __left(self):
        return self.__from_left(0)

    def __top(self):
        return self.__from_top(0)

    def __from_top(self, offset):
        return offset

    def __from_right(self, offset):
        return self.WIDTH - offset

    def __from_left(self, offset):
        return offset

    def __clear_image(self):
        return Image.new('1', (self.WIDTH, self.HEIGHT), 1)

