import requests

city = input('enter the city ')
api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

json_data = requests.get(api).json()

temp = int(json_data['main']['temp'] - 273.15)

pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['wind']['speed']
temp_farhen=(temp*9/5)+32


    
print('The temperature in Celsius is:',temp)
print('The temperature in Fahrenheit is:',temp_farhen)
print('Presure is:',pressure)
print('Humidity is:',humidity)
print('Wind speed is',wind)