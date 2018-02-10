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
import dash
import fetch_build_status
import os

def main():
    epd = epd7in5.EPD()
    epd.init()

    projects = [
        ('PitBuddy iOS', fetch_build_status('https://www.bitrise.io/app/' + os.environ['PB_IOS_APP'] + '.svg?token=' + os.environ['PB_IOS_TOKEN'])),
        ('PitBuddy Android', fetch_build_status('https://www.bitrise.io/app/' + os.environ['PB_ANDROID_APP'] + '.svg?token=' + os.environ['PB_ANDROID_TOKEN'])),
        ('Blog', fetch_build_status('https://circleci.com/gh/hanneskaeufler/blog.svg?style=svg')),
        ('danger-todoist', fetch_build_status('https://travis-ci.org/hanneskaeufler/danger-todoist.svg?branch=master')),
        ('danger-plugin-mentor', fetch_build_status('https://travis-ci.org/hanneskaeufler/danger-plugin-mentor.svg?branch=master'))
    ]

    image = dash.Dash(projects, '/usr/share/fonts/truetype/lato/Lato-Regular.ttf').render(datetime.datetime.now())

    epd.display_frame(epd.get_frame_buffer(image))

    # image = Image.open('monocolor.bmp')
    # epd.display_frame(epd.get_frame_buffer(image))

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)

if __name__ == '__main__':
    main()
