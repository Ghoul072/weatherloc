# WeatherLoc


## What is WeatherLoc
WeatherLoc is a Pythonic API for weather and geolocation, powered by [WeatherAPI](https://www.weatherapi.com/)


## Installation

[WeatherLoc](https://pypi.org/project/WeatherLoc/) is available on PyPI and can be installed via:
```bash
pip install weatherloc
```


## Usage

This package is designed to be as easy as possible to use. Simply create a client object using your API Key as shown below and all commands are available as methods under the newly created client object

```python
import weatherloc

#create a PyWeather client using your API key from www.weatherapi.com
client = weatherloc.Client("YOUR_KEY_HERE")
weather = client.current("London")  # checks and returns current weather
print(weather.condition)            # print current weather condition
print(weather.feelslike_c)          # print feelslike in celsius

# Check the location using an IP address
my_ip = client.ip_lookup("209.142.68.29")
print(my_ip.country_name)

```



## Features
- Get current weather condition
- Future weather predictions upto 300 days from present
- Forecast for days and hours separetely
- Search location by IP address, longitude and latitude, City/Country name, as well as Zip codes and Postcodes
- IP lookup
- Timezone search, get the timezone information for any region
- Astronomical data including sunrise/sunset and moonrise/moonset time, moon phases, and illumination
- Air quality data based on atmospheric gas concentrations and US Gebra and Uk Defra indexes



## Contributing

Pull requests are welcome. For major changes, please open an [issue](https://github.com/Ghoul072/weather/issues) first
to discuss what you would like to change.


## License

MIT
