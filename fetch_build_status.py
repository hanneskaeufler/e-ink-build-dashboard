import urllib2
import dash

def fetch_build_status(url):
    svg = urllib2.urlopen(url).read()

    if 'pass' in svg.lower():
        return dash.BuildStatus.passed

    return dash.BuildStatus.failed
