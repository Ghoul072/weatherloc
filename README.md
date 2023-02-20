# PyWeather Quickstart


## What is PyWeather
PyWeather is a Pythonic API for weather and geolocation, powered by [WeatherAPI](https://www.weatherapi.com/)


<!-- ## Installation

Use [pip](https://pip.pypa.io/en/stable/) package manager to install PyWeather.

```bash
pip install pyweather
``` -->
## Installation
For the time being you can use this package by simply downloading the pyweather folder and keeping it in the same folder as your project, but I'll soon be uploading this to PyPI and upload documentation on readthedocs as well


## Usage

This package is designed to be as easy as possible to use. Simply create a client object using your API Key as shown below and all commands are available as methods under the newly created client object

```python
import pyweather

#create a PyWeather client using your API key from www.weatherapi.com
client = pyweather.Client("YOUR_KEY_HERE")
weather = client.current("London")  # checks and returns current weather
print(weather.condition)            # print current weather condition
print(weather.feelslike_c)          # print feelslike in celsius

# Check the location using an IP address
my_ip = client.ip_lookup("209.142.68.29")
print(my_ip.country_name)

```


## Contributing

Pull requests are welcome. For major changes, please open an [issue](https://github.com/Ghoul072/weather/issues) first
to discuss what you would like to change.


## License

```text
MIT License

Copyright (c) 2023 Yaseen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```