import dash
import datetime
import os


def main():
    projects = [
        ('PitBuddy iOS', dash.BuildStatus.passed),
        ('PitBuddy Android', dash.BuildStatus.passed),
        ('Blog', dash.BuildStatus.failed),
        ('danger-todoist', dash.BuildStatus.passed),
        ('danger-plugin-mentor', dash.BuildStatus.passed)]

    date = datetime.datetime(2018, 2, 10, 1, 1, 1)

    dash.Dash(projects, os.getcwd()).render(date).save('actual.png')


if __name__ == '__main__':
    main()
