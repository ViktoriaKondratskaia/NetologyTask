from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
from django.http import HttpResponse
import csv

with open('BASE_DIR, data-398-2018-08-30.csv),rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)

def index(request):
    return redirect(reverse('bus_stations'))




def bus_stations(request):
    page_number = int(request.get.GET('page',1))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    #district = BUS_STATION_CSV.get(district)
    paginator = Paginator(BUS_STATION_CSV, 10)
    page = paginator.get_page(page_number)
    context = {
       'bus_stations': ...,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
