from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Weather and geolocation API'
LONG_DESCRIPTION = 'Pythonic API for weather and geolocation. Powered by www.weatherapi.com'

# Setting up
setup(
    name="pyweather",
    version=VERSION,
    author="Yaseen",
    author_email="<ahm3d.yaseen@gmail.com>",
    url="https://github.com/Ghoul072/weather",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['pyweather', 'python', 'weather', 'geolocation', 'meteorology', 'api', 'weatherapi'],
    classifiers=[
        "Development Status :: 3 - Alpha Copy",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)