# Gradescope Python Utilities

[![PyPI version](https://badge.fury.io/py/gradescope-utils.svg)](https://badge.fury.io/py/gradescope-utils)
[![Documentation Status](https://readthedocs.org/projects/gradescope-utils/badge/?version=latest)](https://gradescope-utils.readthedocs.io/en/latest/?badge=latest)

## Installing

Make sure you have pip installed (eg. on Debian/Ubuntu, `apt-get install python-pip`).

Then, run `pip install gradescope-utils`

## Packages

- [Autograder Utilities](/gradescope_utils/autograder_utils)

## Changelog

See the [Releases](https://github.com/gradescope/gradescope-utils/releases) page.

## Releasing new versions

Follow https://packaging.python.org/tutorials/packaging-projects/, but in brief:

1. Bump the version in setup.py
2. Draft a release on https://github.com/gradescope/gradescope-utils/releases
  a) This can take care of tagging for you. Otherwise, tag the commit: `git tag vX.Y.Z COMMIT_SHA`
  b) Make sure that the setup.py version matches the tag
3. GitHub Actions will build and publish a new release when a version is tagged.

## Support

Contact us at [help@gradescope.com](mailto:help@gradescope.com) if you need help with these packages.
