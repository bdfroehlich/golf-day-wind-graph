import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

# here we are formatting the PrettyPrinter. Try using different indents!
pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'washington' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()
print(response)

pp.pprint(response)



forecast_list = response['forecast']
today = datetime.now().strftime("%b-%d-%Y")

to_graph = {} # The empty dictionary to store our shaped data
count = 1 # A global iterator to track each day past current datetime

for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count+=1 if current_date <= 31 else 1

# 'forecast': [   {'day': 1, 'temperature': '+22 C', 'wind': '12 km/h'},
#                     {'day': 2, 'temperature': ' C', 'wind': '14 km/h'},
#                     {'day': 3, 'temperature': '5 C', 'wind': ' km/h'}],
#iterate over the 'wind' key for each day in the response and return from default up to indeces 3 (not included) 
# if they wind is '' it is = to 0
    day['wind'] = 0 if day['wind'][0] == ' ' else int(day['wind'][:3])

    to_graph[this_day] = day['wind']

print(to_graph)

# expected output should look something like:
#   {'Aug-24-2021': 12,
#    'Aug-25-2021': 14,  
#    'Aug-26-2021': 0 }

# Remember to always label the axes of your graph!
plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')
print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())

plt.scatter(to_graph.keys(), to_graph.values()) # sets up the graph
plt.show() # paints the graph to your screen


