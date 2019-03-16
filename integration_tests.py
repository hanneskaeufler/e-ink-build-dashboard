import dash
import datetime
import os


def main():
    projects = [
        ('blog', dash.BuildStatus.failed),
        ('crytic', dash.BuildStatus.passed),
        ('danger-plugin-mentor', dash.BuildStatus.passed),
        ('danger-todoist', dash.BuildStatus.passed),
        ('pitbuddy-android', dash.BuildStatus.passed),
        ('pitbuddy-ios', dash.BuildStatus.passed),
    ]

    date = datetime.datetime(2018, 2, 10, 1, 1, 1)

    dash.Dash(projects, os.getcwd()).render(date).save('actual.png')


if __name__ == '__main__':
    main()
