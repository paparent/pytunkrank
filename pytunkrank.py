"""
pytunkrank
==========

An interface to TunkRank API
"""

from urllib import FancyURLopener

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise Exception("A JSON parser is required, e.g., simplejson at " \
                        "http://pypi.python.org/pypi/simplejson/")


version_info = (0, 2)
__version__ = ".".join(map(str, version_info))


_BASE_URI = "http://www.tunkrank.com"


class TunkRankError(Exception):
    pass


class PyTROpener(FancyURLopener):
    version = 'pytunkrank/%s' % (__version__,)


urlopen = PyTROpener().open


def score(username):
    try:
        u = urlopen(_BASE_URI + "/score/%s.json" % (username,))
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
        u = urlopen(_BASE_URI + "/refresh/%s.json" % (username,))
        data = json.loads(u.read())
        return data['refresh']
    except:
        raise TunkRankError("Unable to refresh %s" % (username,))
