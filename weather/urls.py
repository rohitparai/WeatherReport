from django.urls import path
from .views import *
from .view import UKweather

urlpatterns = [  
    path('max_temp/', UKweather.MaxTempAPIView.as_view()),
    path('min_temp/', UKweather.MinTempAPIView.as_view()),
    path('mean_temp/', UKweather.MeanTempAPIView.as_view()),
    path('sunshine_temp/', UKweather.SunshineAPIView.as_view()),
    path('rainfall_temp/', UKweather.RainfallAPIView.as_view()),
    path('rain_days_temp/', UKweather.RainDaysAPIView.as_view()),
    path('air_frost_temp/', UKweather.AirFrostAPIView.as_view()),

]