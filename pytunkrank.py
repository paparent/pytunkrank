"""
pytunkrank
==========

An interface to TunkRank API
"""

import urllib

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise Exception("A JSON parser is required, e.g., simplejson at " \
                        "http://pypi.python.org/pypi/simplejson/")

_BASE_URI = "http://www.tunkrank.com"


class TunkRankError(Exception):
    pass


def score(username):
    try:
        u = urllib.urlopen(_BASE_URI + "/score/%s.json" % (username,))
        data = json.loads(u.read())
        return data['twitter_user']
    except:
        raise TunkRankError("Unable to fetch score for %s" % (username,))


def ranking(username):
    return score(username)["ranking"]


def raw_score(username):
    return score(username)["raw_tunkrank_score"]


def refresh(username):
    try:
        u = urllib.urlopen(_BASE_URI + "/refresh/%s.json" % (username,))
        data = json.loads(u.read())
        return data['refresh']
    except:
        raise TunkRankError("Unable to refresh %s" % (username,))
