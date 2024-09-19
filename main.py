import json
from datetime import datetime
from os import environ

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = environ.get("API_KEY")

start_time = datetime(year=1992, month=7, day=7)
end_time = datetime(year=1992, month=9, day=18)

formated_start_time = datetime.strftime(start_time, "%d-%m-%Y")
formated_end_time = datetime.strftime(end_time, "%d-%m-%Y")

countries_list = ['ua', 'us', 'gb']

url = "https://calendarific.com/api/v2/holidays"

for index in countries_list:
    with open(f"{index}_{formated_start_time}_{formated_end_time}.txt", 'w') as outfile:
        for days in range(1, 32):
            for month in range(7, 10):
                try:
                    response = requests.get(
                        f"{url}?api_key={API_KEY}&country={index}&year=1992&month={month}&day={days}").json()
                    holidays = response["response"]["holidays"]
                    if len(holidays) > 0:
                        for data in holidays:
                            iso = data["date"]["iso"]

                            if start_time.isoformat() <= iso <= end_time.isoformat():
                                json.dump(data, outfile)
                                outfile.write("\n", )

                except KeyError as e:
                    print(f"key not found{e}")
