from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator 
import os
import pathlib

root = pathlib.PurePath(__file__).parent.parent 

file = 'data-398-2018-08-30.csv'
path = os.path.join(root, file)

def index(request):
    return redirect(reverse('bus_stations'))

def get_data():
    bus_stop = []
    with open (path, encoding='utf-8') as data_file:
      reader = csv.reader(data_file, delimiter=',', escapechar = '\\')
      for row in reader:
          dic = {}
          dic['Name'] = row[1]
          dic['Street'] = row[4]  
          dic['District'] = row[5]
          bus_stop.append(dic)
    return (bus_stop[1:])
                  
 

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    data_list = get_data()
    paginator = Paginator(data_list, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    
    context = {
        'bus_stations': paginator,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

# print(path)
# print(root)
# print(get_data())

# dic = {'bus_stations': get_data()}
# for station in dic['bus_stations']:
#     print (station['Name'])
#     print(station['Street'])
#     print(station['District'])