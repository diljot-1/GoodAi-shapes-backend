from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    path('save_locations', views.save_locations),
    path('get_locations', views.get_locations),
    path('get_weather/<str:location_name>', views.get_weather),

    # path('social_links', views.social_links),
]
