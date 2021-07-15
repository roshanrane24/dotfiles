#!/bin/python3

from time import time
import requests as r
import json
import sys
import os


OPENWEATHERAPIKEY = os.environ['OPENWEATHERAPIKEY']
OPENWEATHERLOCATION = os.environ['OPENWEATHERLOCATION']
unit = "standard"


if unit == "metric":
    request_string = "https://api.openweathermap.org/data/2.5/weather?" \
                     f"q={OPENWEATHERLOCATION}&units=metric&" \
                     f"appid={OPENWEATHERAPIKEY}"
elif unit == "metric":
    request_string = f"https://api.openweathermap.org/data/2.5/weather?" \
                     f"q={OPENWEATHERLOCATION}&units=imperial" \
                     f"&appid={OPENWEATHERAPIKEY}"
else:
    request_string = f"https://api.openweathermap.org/data/2.5/weather?" \
                     f"q={OPENWEATHERLOCATION}&appid={OPENWEATHERAPIKEY}"


def get_icon(icon_code):
    url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'
    img = r.get(url)
    res = os.path.join(os.environ["HOME"], ".config/eww/resources")

    if not os.path.exists(res):
        os.mkdir(res)

    fp = os.path.join(res, f"{icon_code}.png")
    with open(fp, 'wb') as file:
        file.write(img.content)
    return fp


cache_path = os.path.join(os.environ["HOME"], ".cache/eww-weather")
now = int(time())

if not os.path.exists(cache_path):
    os.mkdir(cache_path)
    fp = open(os.path.join(cache_path, "1"), "w")
    fp.close()


if (int(os.listdir(cache_path)[0]) not in range(now-600, now+601)):
    response = r.get(request_string)
    if response.ok:
        weather = response.json()
        with open(cache_path + f"{now}", "w") as fp:
            json.dump(weather, fp)
    else:
        print(f"ERROR {response.status_code}")
        sys.exit()
    response.close()
else:
    with open(os.path.join(cache_path, os.listdir(cache_path)[0]), 'r') as fp:
        weather = json.load(fp)


print({
        "temp": round(weather["main"]["temp"]),
        "actual_temp": round(weather["main"]["feels_like"]),
        "pressure": weather["main"]["pressure"],
        "humidity": weather["main"]["humidity"],
        "description": weather["weather"][0]["description"],
        "wind-speed": weather["wind"]["speed"],
        "wind-direction": weather["wind"]["deg"],
        "location": weather["name"],
        "icon": get_icon(weather["weather"][0]["icon"]),
}[sys.argv[1]], end='')
