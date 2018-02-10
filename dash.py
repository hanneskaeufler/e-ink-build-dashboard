from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime

class Dash:
    WIDTH = 640
    HEIGHT = 384

    BLACK = 0
    WHITE = 255

    PADDING = 10
    BADGE_WIDTH = 150

    PROJECTS = [
        ('PitBuddy iOS', True),
        ('PitBuddy Android', True),
        ('Blog', False),
        ('danger-todoist', True),
        ('danger-plugin-mentor', True)]

    PASSED = 'passed'
    FAILED = 'failed'

    def __init__(self):
        self.image = self.__clear_image()
        self.draw = ImageDraw.Draw(self.image)
        self.title_font = ImageFont.truetype('FreeMonoBold.ttf', 32)
        self.font = ImageFont.truetype('Lato-Regular.ttf', 32)
        self.badge_font = ImageFont.truetype('Lato-Regular.ttf', 24)

    def render(self):
        self.__render_header()
        self.__render_rows()

        return self.image

    def __render_header(self):
        self.draw.rectangle(self.__header_rect_pos(), fill = self.BLACK)
        # TODO: Automatical vertical and horizontal centering?
        self.draw.text((self.__from_left(160), self.__from_top(17)),
                       self.__title(),
                       font = self.title_font,
                       fill = self.WHITE)

    def __render_rows(self):
        for index, project in enumerate(self.PROJECTS):
            self.__render_row((index, project[0], project[1]))

    def __render_row(self, row):
        self.__render_project_name(row)
        self.__render_project_status(row)

    def __render_project_status(self, row):
        index = row[0] + 1
        status = row[2]

        if status:
            self.draw.rectangle(self.__badge_position(index), outline = self.BLACK)
            self.draw.text(self.__badge_text_position(index, self.PASSED),
                           self.PASSED,
                           font = self.badge_font,
                           fill = self.BLACK)
        else:
            self.draw.rectangle(self.__badge_position(index), fill = self.BLACK)
            self.draw.text(self.__badge_text_position(index, self.FAILED),
                           self.FAILED,
                           font = self.badge_font,
                           fill = self.WHITE)

    def __badge_text_position(self, index, text):
        width, height = self.draw.textsize(text, font = self.badge_font)
        start_y = index * self.__row_height()
        padding_x = (self.BADGE_WIDTH - width) / 2
        padding_y = (self.__row_height() - height) / 2

        return (self.__from_right(self.BADGE_WIDTH - padding_x + self.PADDING / 2),
                start_y + padding_y)

    def __badge_position(self, index):
        start_y = index * self.__row_height()

        return (self.__from_right(self.BADGE_WIDTH),
                start_y + self.PADDING,
                self.__from_right(self.PADDING),
                start_y + self.__row_height() - self.PADDING)

    def __render_project_name(self, row):
        index = row[0] + 1
        project = row[1]
        guessed_font_vertical_padding = 13
        y_offset = index * self.__row_height() + guessed_font_vertical_padding
        self.draw.text((self.__from_left(self.PADDING), y_offset),
                       project,
                       font = self.font,
                       fill = self.BLACK)

    def __title(self):
        return datetime.date.today().strftime('%B %d, %Y')

    def __header_rect_pos(self):
        return (self.__left(),
                self.__top(),
                self.__right(),
                self.__from_top(1 * self.__row_height()))

    def __row_height(self):
        return self.HEIGHT / (len(self.PROJECTS) + 1)

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

