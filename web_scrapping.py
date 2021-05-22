import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YJIz-LUzZPY')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_='tombstone-container')

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

#Output
# Tonight
# Patchy Fog
# Low: 59 °F

#list comprehension
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

#period_names = [item.find(class_='period-name').get_text() for item in items]
#short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
#temperatures = [item.find(class_='temp').get_text() for item in items]
# this is equal to
# item_list = []
# for item in items:
#     item_list.append(item.find(class_='period-name').get_text())
# print(item_list)

# print(period_names)
# print(short_descriptions)
# print(temperatures)
#Output
# ['Tonight', 'Wednesday', 'WednesdayNight', 'Thursday', 'ThursdayNight', 'Friday', 'FridayNight', 'Saturday', 'SaturdayNight']
# ['Patchy Fog', 'Patchy Fogthen Sunny', 'Patchy Fog', 'Patchy Fogthen Sunny', 'Patchy Fog', 'Patchy Fogthen Sunny', 'Patchy Fog', 'Patchy Fogthen Sunny', 'Patchy Fog']
# ['Low: 59 °F', 'High: 81 °F', 'Low: 59 °F', 'High: 78 °F', 'Low: 58 °F', 'High: 77 °F', 'Low: 56 °F', 'High: 77 °F', 'Low: 57 °F'] °F', 'High: 77 °F', 'Low: 56 °F', 'High: 77 °F', 'Low: 57 °F']

whether_info = pd.DataFrame(
    {'Period': period_names,
     'Description': short_descriptions,
     'Temperature': temperatures,    #Always add comma (,) after last entry in dictionary. it wont give error and help you in future when you add new entry
    })

print(whether_info)

#pandas have this amazing feature to export this to a csv or any other file
whether_info.to_csv('whether.csv')