import epd7in5
import datetime
import dash
from fetch_build_status import fetch_build_status
import os


def main():
    epd = epd7in5.EPD()
    epd.init()

    projects = [
        ('PitBuddy iOS', fetch_build_status('https://www.bitrise.io/app/' + os.environ['PB_IOS_APP'] + '.svg?token=' + os.environ['PB_IOS_TOKEN'])),  # noqa
        ('PitBuddy Android', fetch_build_status('https://www.bitrise.io/app/' + os.environ['PB_ANDROID_APP'] + '.svg?token=' + os.environ['PB_ANDROID_TOKEN'])),  # noqa
        ('Blog', fetch_build_status('https://circleci.com/gh/hanneskaeufler/blog.svg?style=svg')),  # noqa
        ('danger-todoist', fetch_build_status('https://travis-ci.org/hanneskaeufler/danger-todoist.svg?branch=master')),  # noqa
        ('danger-plugin-mentor', fetch_build_status('https://travis-ci.org/hanneskaeufler/danger-plugin-mentor.svg?branch=master'))  # noqa
    ]

    image = (
        dash
        .Dash(projects, '/usr/share/fonts/truetype/lato/Lato-Regular.ttf')
        .render(datetime.datetime.now())
    )

    epd.display_frame(epd.get_frame_buffer(image))


if __name__ == '__main__':
    main()
