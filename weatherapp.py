import requests

# Open weather API key
api_key = "add-key"

# Input city you'd like to see weather for
city = input('City: ')

# URL we use in our HTTP request, using our api key and city values.
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Make request to openweathermap, store response body in response variable.
response = requests.get(url)

if response.status_code == 200:
    # Read the response body as JSON data and store in data variable which now
    # Contains a python dictionary.
    data = response.json()
    # Subtract 273.15 from kelvin value to get celcius
    temp = data['main']['temp'] - 273.15
    desc = data['weather'][0]['description']
    print(f"{data}")
    # print our temperature from 'main' dictionary using the key 'temp', convert
    # to integer number
    print(f'Temperature: {int(temp)} C')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
