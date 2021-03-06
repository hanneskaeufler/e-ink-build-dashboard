from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from enum import Enum
import os


class BuildStatus(Enum):
    passed = 1
    failed = 2


class Dash:
    WIDTH = 640
    HEIGHT = 384

    BLACK = 0
    WHITE = 255

    PADDING = 10
    BADGE_WIDTH = 70

    PASSED = u'\uf058'
    FAILED = u'\uf057'

    def __init__(self, projects, fonts_dir):
        self.projects = projects
        self.image = self.__clear_image()
        self.draw = ImageDraw.Draw(self.image)
        self.title_font = ImageFont.truetype(
            os.path.join(fonts_dir, 'lato', 'Lato-Black.ttf'), 32)
        self.font = ImageFont.truetype(
            os.path.join(fonts_dir, 'lato', 'Lato-Regular.ttf'), 32)
        self.badge_font = ImageFont.truetype(
            os.path.join(fonts_dir, 'lato', 'Lato-Regular.ttf'), 24)
        self.icon_font = ImageFont.truetype(
            os.path.join(fonts_dir, 'fontawesome', 'fa-regular-400.ttf'), 24)

    def render(self, date):
        self.__render_header(date)
        self.__render_rows()

        return self.image

    def __render_header(self, date):
        self.draw.rectangle(self.__header_rect_pos(), fill=self.BLACK)
        title = self.__title(date)
        width, height = self.draw.textsize(title, font=self.title_font)
        self.draw.text((self.__from_left(self.WIDTH / 2 - width / 2),
                        self.__from_top(self.__row_height() / 2 - height / 2)),
                       self.__title(date),
                       font=self.title_font,
                       fill=self.WHITE)

    def __render_rows(self):
        for index, project in enumerate(self.projects):
            self.__render_row((index, project[0], project[1]))

    def __render_row(self, row):
        self.__render_project_name(row)
        self.__render_project_status(row)

    def __render_project_status(self, row):
        index = row[0] + 1
        status = row[2]

        if status == BuildStatus.passed:
            self.draw.rectangle(self.__badge_position(index),
                                outline=self.BLACK)
            self.__draw_badge_icon(index, self.PASSED, self.BLACK)
        else:
            self.draw.rectangle(self.__badge_position(index), fill=self.BLACK)
            self.__draw_badge_icon(index, self.FAILED, self.WHITE)

    def __draw_badge_icon(self, index, text, color):
        self.draw.text(self.__badge_text_position(index, text),
                       text,
                       font=self.icon_font,
                       fill=color)

    def __badge_text_position(self, index, text):
        width, height = self.draw.textsize(text, font=self.icon_font)
        start_y = index * self.__row_height()
        padding_x = (self.BADGE_WIDTH - width) / 2
        padding_y = (self.__row_height() - height) / 2
        offset_x = self.BADGE_WIDTH - padding_x + self.PADDING / 2

        return (self.__from_right(offset_x), start_y + padding_y)

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
                       font=self.font,
                       fill=self.BLACK)

    def __title(self, date):
        return date.strftime('%c')

    def __header_rect_pos(self):
        return (self.__left(),
                self.__top(),
                self.__right(),
                self.__from_top(1 * self.__row_height()))

    def __row_height(self):
        return self.HEIGHT / (len(self.projects) + 1)

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
