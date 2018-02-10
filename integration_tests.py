import dash
import os

def main():
    projects = [
        ('PitBuddy iOS', dash.BuildStatus.passed),
        ('PitBuddy Android', dash.BuildStatus.passed),
        ('Blog', dash.BuildStatus.failed),
        ('danger-todoist', dash.BuildStatus.passed),
        ('danger-plugin-mentor', dash.BuildStatus.passed)]

    dash.Dash(projects, os.getcwd()).render().save('actual.png')

if __name__ == '__main__':
    main()
