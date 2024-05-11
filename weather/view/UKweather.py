from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import csv
from io import StringIO


class MaxTempAPIView(APIView):
    def get(self, request, format=None):
        max_temp_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/ranked/UK.txt"
        max_temp_response = requests.get(max_temp_url)
        max_temp_data = max_temp_response.text

        # Parse the CSV data
        max_temp_records = []
        lines = max_temp_data.split('\n')
        column_titles = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for line in lines[8:]:  # Skip header and title lines
            values = line.split()
            if len(values) > 0:
                year = values.pop(0)  # Extract year from the beginning of the line
                max_temp_year_data = []
                for month, temp in zip(column_titles, values):
                    try:
                        temp_value = float(temp)
                    except ValueError:
                        temp_value = None
                    max_temp_year_data.append({"temp": temp_value, "month": month, "year": year})
                max_temp_records.append(max_temp_year_data)

        return Response(max_temp_records)


class MinTempAPIView(APIView):
    def get(self, request, format=None):
        min_temp_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/ranked/UK.txt"
        min_temp_response = requests.get(min_temp_url)
        min_temp_data = min_temp_response.text

        # Parse the CSV data
        min_temp_records = []
        lines = min_temp_data.split('\n')
        for line in lines[8:]:  # Skip header and title lines
            min_temp_year_data = []
            values = line.split()
            for i in range(0, len(values), 2):
                year = values[i + 1]  # Get the year value
                if year:  # Check if year data is not empty
                    min_temp_year_data.append({"temp": values[i], "year": int(year)})
            min_temp_records.append(min_temp_year_data)

        return Response(min_temp_records)


class MeanTempAPIView(APIView):
    def get(self, request, format=None):
        mean_temp_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/ranked/UK.txt"
        mean_temp_response = requests.get(mean_temp_url)
        mean_temp_data = mean_temp_response.text

        # Parse the CSV data
        mean_temp_records = []
        lines = mean_temp_data.split('\n')
        for line in lines[8:]:  # Skip header and title lines
            mean_temp_year_data = []
            values = line.split()
            for i in range(0, len(values), 2):
                year = values[i + 1]  # Get the year value
                if year:  # Check if year data is not empty
                    mean_temp_year_data.append({"temp": values[i], "year": int(year)})
            mean_temp_records.append(mean_temp_year_data)

        return Response(mean_temp_records)


class SunshineAPIView(APIView):
    def get(self, request, format=None):
        sunshine_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/ranked/UK.txt"
        sunshine_response = requests.get(sunshine_url)
        sunshine_data = sunshine_response.text

        # Parse the CSV data
        sunshine_records = []
        lines = sunshine_data.split('\n')
        for line in lines[8:]:  # Skip header and title lines
            sunshine_year_data = []
            values = line.split()
            for i in range(0, len(values), 2):
                year = values[i + 1]  # Get the year value
                if year:  # Check if year data is not empty
                    sunshine_year_data.append({"hours": values[i], "year": int(year)})
            sunshine_records.append(sunshine_year_data)

        return Response(sunshine_records)


class RainfallAPIView(APIView):
    def get(self, request, format=None):
        rainfall_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/ranked/UK.txt"
        rainfall_response = requests.get(rainfall_url)
        rainfall_data = rainfall_response.text

        # Parse the CSV data
        rainfall_records = []
        lines = rainfall_data.split('\n')
        for line in lines[8:]:  # Skip header and title lines
            rainfall_year_data = []
            values = line.split()
            for i in range(0, len(values), 2):
                year = values[i + 1]  # Get the year value
                if year:  # Check if year data is not empty
                    rainfall_year_data.append({"mm": values[i], "year": int(year)})
            rainfall_records.append(rainfall_year_data)

        return Response(rainfall_records)


class RainDaysAPIView(APIView):
    def get(self, request, format=None):
        rain_days_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Raindays1mm/ranked/UK.txt"
        rain_days_response = requests.get(rain_days_url)
        rain_days_data = rain_days_response.text

        # Parse the CSV data
        rain_days_records = []
        lines = rain_days_data.split('\n')
        for line in lines[8:]:  # Skip header and title lines
            rain_days_year_data = []
            values = line.split()
            for i in range(0, len(values), 2):
                year = values[i + 1]  # Get the year value
                if year:  # Check if year data is not empty
                    rain_days_year_data.append({"days": values[i], "year": int(year)})
            rain_days_records.append(rain_days_year_data)

        return Response(rain_days_records)


class AirFrostAPIView(APIView):
    def get(self, request, format=None):
        air_frost_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/AirFrost/ranked/UK.txt"
        air_frost_response = requests.get(air_frost_url)
        air_frost_data = air_frost_response.text

        # Parse the CSV data
        air_frost_records = []
        lines = air_frost_data.split('\n')
        for line in lines[8:]:  # Skip header and title lines
            air_frost_year_data = []
            values = line.split()
            for i in range(0, len(values), 2):
                year = values[i + 1]  # Get the year value
                if year:  # Check if year data is not empty
                    air_frost_year_data.append({"days": values[i], "year": int(year)})
            air_frost_records.append(air_frost_year_data)

        return Response(air_frost_records)
