import urllib2
import dash

def fetch_build_status(url):
    svg = urllib2.urlopen(url).read()

    if 'passing' in svg:
        return dash.BuildStatus.passed

    return dash.BuildStatus.failed
