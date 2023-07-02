#!/usr/bin/python3
"""
This codefetches https://alx-intranet.hbtn.io/status
using urllib package
"""
import urllib.request

if __name__ == '__main__':
    reqs = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(reqs) as response:
        webContent = response.read()

    print("Body response:")
    print("\t- type: {}".format(webContent.__class__))
    print("\t- content: {}".format(webContent))
    print("\t- utf8 content: {}".format(webContent.decode('ascii')))
