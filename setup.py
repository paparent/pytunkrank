from distutils.core import setup

setup(name='pytunkrank',
      version='0.1',
      author='PA Parent',
      author_email='paparent@paparent.me',
      description='Python interface to TunkRank API',
      long_description="""
pytunkrank
==========

Python interface to the [TunkRank API](http://tunkrank.com/api).  [TunkRank](http://tunkrank.com) is a tool that measures a person's influence on Twitter by looking at how much attention your followers can actually give you.  You can read more [here](http://tunrkank.com/about).

Ported from Jason Adams' ruby gem [tunkrank](http://github.com/ealdent/tunkrank).

Usage
-----

The TunkRank API supports two main methods:  `score` and `refresh`.  The module includes two convenience methods for returning just the raw score or just the ranking.

    import pytunkrank
    pytunkrank.score('ealdent')
    pytunkrank.raw_score('ealdent')  # => 6.87
    pytunkrank.ranking('ealdent')    # => 21
    pytunkrank.refresh('ealdent')

Copyright
---------

Copyright (c) 2010 pytunkrank Authors (as specified in AUTHORS file). See LICENSE for details.

Original work from Jason Adams' ruby gem [tunkrank](http://github.com/ealdent/tunkrank).
""",
      license="MIT",
      url="http://github.com/paparent/pytunkrank",
      py_modules=['pytunkrank'],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: MIT License",
      ],
     )
