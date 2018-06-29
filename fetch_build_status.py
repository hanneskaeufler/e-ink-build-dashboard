import dash
import re
import urllib2


def fetch_build_status(url):
    svg_or_json = urllib2.urlopen(url).read()

    if re.search('pass|success', svg_or_json.lower()):
        return dash.BuildStatus.passed

    return dash.BuildStatus.failed
