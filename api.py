import pandas as pd
import requests
import csv
csv_file = 'Cities.csv'
header = ['Sl no', 'City', 'region',
          'latitude(lat)', 'longitude(lon)', 'temperature in deg(temp_c)', 'wind_kph', 'wind_direction']
df = pd.read_csv(csv_file)
dic = dict()
for i in range(len(df)):
    city = df.at[i, 'City Name']
    dic[i] = city

data=[]
counter = 1
for i in dic.values():
    res = requests.get(
        f'https://api.weatherapi.com/v1/current.json?key=c005e90249e54c2e921141433211709&q={i}&aqi=no')
    weather = res.json()
    sl = counter
    counter = counter + 1
    city = weather['location']['name']
    region = weather['location']['region']
    lat = weather['location']['lat']
    lon = weather['location']['lon']
    temp = weather['current']['temp_c']
    wkph = weather['current']['wind_kph']
    wind_dir = weather['current']['wind_dir']
    w=[sl,city,region,lat,lon,temp,wkph,wind_dir]
    data.append(w)
    
    
with open('cities_with_values.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)