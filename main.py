import epd7in5
import datetime
import dash
from fetch_build_status import fetch_build_status
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def fetch_bitrise_build_status(app, token):
    return fetch_build_status(
        'https://app.bitrise.io/app/' + app + '/status.json?token=' + token)


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
        ('blog', fetch_circle_build_status('blog')),
        ('crytic', dash.BuildStatus.passed),
        ('danger-todoist', fetch_travis_build_status('danger-todoist')),
        ('danger-plugin-mentor', fetch_travis_build_status('danger-plugin-mentor')),  # noqa
        ('pitbuddy-ios', fetch_bitrise_build_status(os.getenv('PB_IOS_APP'), os.getenv('PB_IOS_TOKEN'))),  # noqa
        ('pitbuddy-android', fetch_bitrise_build_status(os.getenv('PB_ANDROID_APP'), os.getenv('PB_ANDROID_TOKEN')))  # noqa
    ]

    image = (
        dash
        .Dash(projects, os.getenv('DASH_FONTS_DIR'))
        .render(datetime.datetime.now())
    )

    epd.display_frame(epd.get_frame_buffer(image))


if __name__ == '__main__':
    main()
