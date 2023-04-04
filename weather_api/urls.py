from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('get_random_dimension', views.get_random_dimension),

    # path('social_links', views.social_links),
]
