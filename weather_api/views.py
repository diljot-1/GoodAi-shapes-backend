from django.shortcuts import render, redirect
from weather_api.key import api_key
import requests
from django.http import HttpResponse
import math
import random
import json
from .models import Location

# Create your views here.

def index(request):
    return render(request, "weather_api/home.html")




def get_random_dimension(request, *args, **kwargs):
    random_value = random.uniform(1.0, 10.0)
    rounded_value = round(random_value, 2)

    response_object = {
        "message": 'random value generated',
        "value": rounded_value
    }

    return HttpResponse( json.dumps( response_object ) )




# class Test {

#     public static void demo(int i){


#     }
# }

# Class Test2 extends Test
# {
#     public static void demo(){

#     }
# }

# Class Animal {

#     def Animal(self, id):
#         return ""
# }

# class Animal : public

#     def AnimalType(self, id):
#         return 1

#     def AnimalName(self, name):
#         return 