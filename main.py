##
 #  @filename   :   main.cpp
 #  @brief      :   7.5inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 28 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

import epd7in5
import Image
import ImageDraw
import ImageFont
import datetime
#import imagedata
import codecs

EPD_WIDTH = 640
EPD_HEIGHT = 384
BLACK = 0
WHITE = 255
ROW = EPD_HEIGHT / 6

def from_left(offset):
    return 0 + offset

def from_right(offset):
    return EPD_WIDTH + offset

def row(draw, text, index, passed):
    guessed_font_padding = 13
    padding = 10
    font = ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Regular.ttf', 32)
    icon_font = ImageFont.truetype('/home/pi/demo/fontawesome/web-fonts-with-css/webfonts/fa-regular-400.ttf', 32)
    draw.text((from_left(padding), index*ROW + guessed_font_padding), text, font = font, fill = BLACK)
    badge(draw, index*ROW, passed)

def badge(draw, start_y, passed):
    badge_width = 150
    padding = 10
    pos = (from_right(-badge_width), start_y + padding, from_right(-padding), start_y + ROW - padding)
    font = ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Regular.ttf', 24)
    inner_padding = 5

    if passed:
        draw.rectangle(pos, outline = BLACK)
        draw.text((from_right(-badge_width + 35), start_y + 17), 'passed', font = font, fill = BLACK)
    else:
        draw.rectangle(pos, fill = BLACK)
        draw.text((from_right(-badge_width + 40), start_y + 17), 'failed', font = font, fill = WHITE)

def main():
    epd = epd7in5.EPD()
    epd.init()
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 32)

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    draw = ImageDraw.Draw(image)

    #draw.rectangle((0, 6, EPD_WIDTH, EPD_HEIGHT), fill = 0)

    # header
    draw.rectangle((from_left(0), 0*ROW, EPD_WIDTH, 1*ROW), fill = BLACK)
    draw.text((from_left(160), 0*ROW + 17), datetime.date.today().strftime("%B %d, %Y"), font = font, fill = WHITE)

    row(draw, 'PitBuddy iOS', 1, True)
    row(draw, 'PitBuddy Android', 2, True)
    row(draw, 'Blog', 3, False)
    row(draw, 'danger-todoist', 4, True)
    row(draw, 'danger-plugin-mentor', 5, True)

    #draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    #draw.rectangle((0, 80, 160, 280), fill = 255)
    #draw.arc((40, 80, 180, 220), 0, 360, fill = 0)

    epd.display_frame(epd.get_frame_buffer(image))

    # image = Image.open('monocolor.bmp')
    # epd.display_frame(epd.get_frame_buffer(image))

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)

if __name__ == '__main__':
    main()
