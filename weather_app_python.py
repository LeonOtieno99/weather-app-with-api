import requests

print('*************************')
print('*    Weather App        *')
print('*************************')

print('\nTo receive your weather forecast')
city = input('Enter your city name?\n')

#your api key from open weather
api_key = " "

base_url = "http://api.openweathermap.org/data/2.5/weather?"

complete_url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(complete_url)

#convert data to json format for easy reading
data = response.json()

#check if cod == 200
if data["cod"] != "404":

    #collect data from dictionary labelled main
    specific = data["main"]
    temperature = specific["temp"]
    pressure = specific["pressure"]
    humidity = specific["humidity"]

    country = data["sys"]
    country_acro = country["country"]

    weather = data["weather"]
    #weather descripton is a dictionary in a list
    weather_description = weather[0]["description"]

else:
    print(f'{city} city  not found')

#print the data
print(f'In {city}:')
print(f'Found in {country_acro}')
print(f'The temperature is: {temperature:.2f} Kelvin')
print(f'The pressure is: {pressure:.2f} Pa')
print(f'The humidity is: {humidity:.2f}%')
print(f'The weather is: {weather_description}')


