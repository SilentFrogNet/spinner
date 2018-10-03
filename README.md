[![GitHub tag](https://img.shields.io/github/tag/SilentFrogNet/spinner.svg?label=version)](https://github.com/SilentFrogNet/spinner/releases)
[![GitHub license](https://img.shields.io/github/license/SilentFrogNet/spinner.svg)](https://github.com/SilentFrogNet/spinner/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/SilentFrogNet/spinner)
[![GitHub issues](https://img.shields.io/github/issues/SilentFrogNet/spinner.svg)](https://github.com/SilentFrogNet/spinner/issues)


# Spinner

This is a really tiny library to add spinners to your code.


## Install 

From git

`pip install git+git://github.com/SilentFrogNet/spinner.git`


## Spinner types

These are the available `SpinnerTypes`

  | Name          | Example                                                         |
  | ---           | ---                                                             |
  | CLASSIC       | ![](https://media.giphy.com/media/Zcxo127Rk8lCKhcyCJ/giphy.gif) |
  | SINGLE_PIPES  | ![](https://media.giphy.com/media/tsStoop09Dl5SvCcu2/giphy.gif) |
  | DOUBLE_PIPES  | ![](https://media.giphy.com/media/cIjNu8vDhtkoSa1jPx/giphy.gif) |
  | VERTICAL      | ![](https://media.giphy.com/media/1qgIRgTLgi0XBobx4h/giphy.gif) |
  | DOT           | ![](https://media.giphy.com/media/5h5D8vGsYIHcS8psJt/giphy.gif) |
  | DOTS          | ![](https://media.giphy.com/media/ZxYt3xY2faI5udsiLQ/giphy.gif) |
  | DOTS2         | ![](https://media.giphy.com/media/8vqEO6bwmsd95F1BDr/giphy.gif) |


## Example of use

Check the `spin_test.py` file for a working example.

``` python
from spinner import Spinner, SpinnerTypes

with Spinner(prefix="my awesome spinner...", spinner_type=SpinnerTypes.VERTICAL):
    time.sleep(5)   # Any of your time-consuming task
```


# Changelog

What's happened so far...


## 1.1.0 - 2018-10-03

### Changed

 *  Simplified the use of the spinner with python context manager


## 1.0.1 - 2018-09-10

### Added

 *  Added examples into the README file


## 1.0.0 - 2018-09-10

 *  First stable release
