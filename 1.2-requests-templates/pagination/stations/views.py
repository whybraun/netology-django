import csv
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station_info = {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
            bus_stations.append(station_info)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
