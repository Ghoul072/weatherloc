from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.2'
DESCRIPTION = 'Weather and geolocation API'
LONG_DESCRIPTION = 'Pythonic API for weather and geolocation. Powered by www.weatherapi.com'

# Setting up
setup(
    name="WeatherLoc",
    version=VERSION,
    author="Yaseen",
    author_email="<ahm3d.yaseen@gmail.com>",
    url="https://github.com/Ghoul072/pyweather",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["requests==2.28.2", "charset-normalizer", "urllib3", "idna", "certifi"],
    keywords=['weatherloc', 'python', 'weather', 'geolocation', 'meteorology', 'api', 'weatherapi', 'pyweather', 'python-weather', 'science', 'pyweather', 'ip', 'ip-finder', 'location'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)