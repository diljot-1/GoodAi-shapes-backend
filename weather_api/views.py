from django.shortcuts import render, redirect
from weather_api.key import api_key
import requests
from django.http import HttpResponse
import math
from .models import Location

# Create your views here.

def index(request):
    return render(request, "weather_api/home.html")




def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        w_dataset = requests.get(url).json()
        try:
            context = {
                ####
                "city_name":w_dataset["city"]["name"],
                "city_country":w_dataset["city"]["country"],
                "wind":w_dataset['list'][0]['wind']['speed'],
                "degree":w_dataset['list'][0]['wind']['deg'],
                "status":w_dataset['list'][0]['weather'][0]['description'],
                "cloud":w_dataset['list'][0]['clouds']['all'],
                'date':w_dataset['list'][0]["dt_txt"],
                'date1':w_dataset['list'][1]["dt_txt"],
                'date2':w_dataset['list'][2]["dt_txt"],
                'date3':w_dataset['list'][3]["dt_txt"],
                'date4':w_dataset['list'][4]["dt_txt"],
                'date5':w_dataset['list'][5]["dt_txt"],
                'date6':w_dataset['list'][6]["dt_txt"],


                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(w_dataset["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(w_dataset["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(w_dataset["list"][6]["main"]["temp_max"] -273.0),


                "pressure":w_dataset["list"][0]["main"]["pressure"],
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "sea_level":w_dataset["list"][0]["main"]["sea_level"],


                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],
                "icon":w_dataset["list"][0]["weather"][0]["icon"],
                "icon1":w_dataset["list"][1]["weather"][0]["icon"],
                "icon2":w_dataset["list"][2]["weather"][0]["icon"],
                "icon3":w_dataset["list"][3]["weather"][0]["icon"],
                "icon4":w_dataset["list"][4]["weather"][0]["icon"],
                "icon5":w_dataset["list"][5]["weather"][0]["icon"],
                "icon6":w_dataset["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')


def get_locations(request, *args, **kwargs):
        url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=f3efe3a5-9f32-46ce-8729-89a9f6e02248'
        
        r =  requests.get(url, headers={'Content-Type': 'text/json'})
        res = r.json()
        return HttpResponse(r, content_type='text/json')


def get_weather(request,location_name, **kwargs):
    url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/'
    
    location_object = Location.objects.get(name=location_name)
    location_id = location_object.met_office_location_id
   
    url = url + str(location_id) + '?res=3hourly&key=f3efe3a5-9f32-46ce-8729-89a9f6e02248'
    r =  requests.get(url, headers={'Content-Type': 'text/json'})

    return HttpResponse(r, content_type='text/json')


def save_locations(request, *args, **kwargs):
    url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=f3efe3a5-9f32-46ce-8729-89a9f6e02248'
        
    r =  requests.get(url, headers={'Content-Type': 'text/json'})
    res = r.json()

    all_location_objects = []
    # print(res['Locations'])
    for location in res['Locations']['Location']:
        print(location['name'])
        all_location_objects.append(
            Location(
                name=location['name'],
                met_office_location_id=location['id'],
                latitude=location['latitude'],
                longitude=location['longitude']
                )
            )
    
    locations = Location.objects.bulk_create(all_location_objects)
    return HttpResponse(r, content_type='text/json')

# def social_links(request):
#     sl = Social.objects.all()
#     context = {
#         'sl': sl
#     }
#     return render(request, 'weather_api/base.html', context)
