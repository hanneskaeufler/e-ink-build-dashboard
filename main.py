import epd7in5
import datetime
import dash
from fetch_build_status import fetch_build_status
import os


def fetch_bitrise_build_status(app, token):
    return fetch_build_status(
        'https://www.bitrise.io/app/' + app + '.svg?token=' + token)


def fetch_travis_build_status(repo):
    return fetch_build_status(
        'https://travis-ci.org/hanneskaeufler/' + repo + '.svg?branch=master')


def fetch_circle_build_status(repo):
    return fetch_build_status(
        'https://circleci.com/gh/hanneskaeufler/' + repo + '.svg?style=svg')


def main():
    epd = epd7in5.EPD()
    epd.init()

    projects = [
        ('PitBuddy iOS', fetch_bitrise_build_status(os.environ['PB_IOS_APP'], os.environ['PB_IOS_TOKEN'])),  # noqa
        ('PitBuddy Android', fetch_bitrise_build_status(os.environ['PB_ANDROID_APP'], os.environ['PB_ANDROID_TOKEN'])),  # noqa
        ('Blog', fetch_circle_build_status('blog')),
        ('danger-todoist', fetch_travis_build_status('danger-todoist')),
        ('danger-plugin-mentor', fetch_travis_build_status('danger-plugin-mentor'))  # noqa
    ]

    image = (
        dash
        .Dash(projects, '/usr/share/fonts/truetype/lato/Lato-Regular.ttf')
        .render(datetime.datetime.now())
    )

    epd.display_frame(epd.get_frame_buffer(image))


if __name__ == '__main__':
    main()
