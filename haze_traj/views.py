from django.shortcuts import render
from .models import Haze_traj_db
from .models import HotspotSipongi
import pysplit
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
import ast
from .forms import HazeInitialForm
from .tables import HotspotTable
from django_tables2 import SingleTableView

from django_tables2 import RequestConfig
from django_filters.views import FilterView
import tablib
import csv

from .filters import HotspotFilter
    
def about(request):             #halaman about
    return render (request, 'haze_traj/about.html')
    
def index(request):             #halaman utama
    return render (request, 'haze_traj/index.html')

import tablib
import csv
from django.http import HttpResponse


def download_table(table, file_format, filename):
    dataset = tablib.Dataset()
    dataset.headers = [column.verbose_name for column in table.columns]
    for row in table.rows:
        dataset.append(list(row))  # Convert the row to a list

    if file_format == 'csv':
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
    elif file_format == 'txt':
        response = HttpResponse(dataset.csv, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{filename}.txt"'
    else:
        response = HttpResponse("Invalid file format.")

    return response


# filter_table = HotspotFilter(request.GET, queryset=qs)  # Apply the filter

def filtering_input(request):
    print(request.GET)
    qs = filter(request)
    # qs = {}
    # if 'download' not in request.GET: 
    #     qs = filter(request)
    print(qs)
    table = HotspotTable(qs)
    # print(qs[:5].__str__())
    table.paginate(page=request.GET.get("page", 1), per_page=10)  #Paginate the table
    RequestConfig(request, paginate={"per_page": 10}).configure(table)  #Configure table pagination

    for item in qs:
        print(item.lat)
        # tanggal_waktu = item.date_hotspot_ori
        # # str_tanggal_waktu= str(tanggal_waktu)
        # # splittedDateTime_partition= str_tanggal_waktu.split('+')
        # # print('ini string',splittedDateTime_partition[0])
        # # print('ini datefield',tanggal_waktu)
        # date_fix = str(tanggal_waktu)
        # splittedDateTime= date_fix.split(' ')
        # splittedDate=splittedDateTime[0]
        # splittedTime=splittedDateTime[1]
        # print('ini tanggal',splittedDate)
        # print('ini waktu',splittedTime)
    
    m = folium.Map(zoom_start=4.5 , location=[-3.0893, 117.9213])
    
    if request.method == "POST":
        print(request.POST.get('format'))
        form = HazeInitialForm(request.POST)
        if request.POST.get('type')== 'download':
            file_format = request.POST.get('format')
            filename = 'table_export'
            response = download_table(table, file_format, filename)
            return response
        elif request.POST.get('type')=='generate_traj':
            if form.is_valid():
            
                altitudes = [int(form.cleaned_data['altitude_input'])]         
                runtime = int(form.cleaned_data['runtime_input'])
                
                basename = 'colgate'
                
                for item in qs: 
                        print(item)
                        provinsi = item.nama_provinsi
                        kab_kota = item.kabkota
                        kecamatan = item.kecamatan
                        desa = item.desa
                        tanggal_waktu = item.date_hotspot_ori
                        satelit = item.sumber
                        confidence = item.confidence_level
                        latitude = item.lat
                        longitude = item.long
                        
                        location = (latitude, longitude)
                        
                        date_fix = str(tanggal_waktu)
                        splittedDateTime= date_fix.split(' ')
                        splittedDate=splittedDateTime[0]
                        splittedTime=splittedDateTime[1]
                        # print('ini tanggal',splittedDate)
                        # print('ini waktu',splittedTime)
                        
                        str_splittedTime=str(splittedTime)
                        # print('str split time', str_splittedTime)
                        
                        working_dir = r'/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/working'
                        storage_dir = r'/home/noval/Kuliah/App Haze/colgate'
                        meteo_dir = r'/home/noval/Kuliah/App Haze/meteo'
                        splittedDate=splittedDateTime[0]
                        splittedDate_part= splittedDate.split('-')
                        years = [int(splittedDate_part[0])]
                        months = [int(splittedDate_part[1])]
                        
                        str_splittedTime_part= str_splittedTime.split(':')
                        hours = [int(str_splittedTime_part[0])]
                        # print('hours int', hours)
                        # print('str hours',str_splittedTime_part[0])
                        
                        str_coordinates=''.join(str(num).replace('.', '').replace(',', '') for num in location)
                        # print('str coords', str_coordinates)
                    
                        filter_path=splittedDate_part[0]+splittedDate_part[1]+splittedDate_part[2]+str_splittedTime_part[0]+str_coordinates

                        pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                                                    years, months, hours, altitudes, location, runtime,
                                                    monthslice=slice(int(splittedDate_part[2])-1, int(splittedDate_part[2]), 1), get_reverse=False,
                                                    get_clipped=False, hysplit = "/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/exec/hyts_std")

                        str_altitudes = ''.join(str(num).replace('.', '') for num in altitudes)
                        #visual
                        print(filter_path)
                        path = '/home/noval/Kuliah/App Haze/colgate/'+'*'+str_altitudes+'*'+filter_path+'*'
                        print('path is', path)
                        trajgroup = pysplit.make_trajectorygroup((path))

                        for traj in trajgroup[::5]:
                            line = traj.path
                            print(list(line.coords))
                            lists=list(line.coords)
                            print('list=', lists)

                            result=[]
                            for tpl in lists:
                                result.append(tpl[:2])
                                    
                            new_list=[(t[1], t[0]) for t in result]        
                            print("result")
                            print(new_list)
                            print('testt')
                            
                            final_latlong=[]
                            for x, y, z in line.coords:
                                latlongs= ('({}, {})'. format(y,x,z))
                                final_latlong.append(latlongs)

                            trail_coordinates = [
                                new_list
                                ]
                            
                            if confidence == 'Low':
                                color = 'green'
                            elif confidence == 'low':
                                color = 'green'
                            elif confidence == 'Medium':
                                color = 'orange'
                            elif confidence == 'medium':
                                color = 'orange'
                            else:
                                color = 'red'
                                
                            
                            folium.PolyLine(trail_coordinates, tooltip=new_list[0], color=color).add_to(m)
                            
                            for i in range(1, len(new_list)):
                                dot_icon = folium.CustomIcon(
                                icon_image=f'data:image/svg+xml;utf-8,<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="{color}" /></svg>',
                                icon_size=(5, 5))
                                
                                #print(tanggal_waktu,'ini datefixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                                #print(type(tanggal_waktu))
                                tanggal_waktu += timedelta(minutes=30)
                                #print(tanggal_waktu, 'ini stardate############################################')
                                
                                date_component = tanggal_waktu.date()
                                time_component = tanggal_waktu.time()
                                #print(date_component, 'ini date_component############################################')
                                print(time_component, 'ini time_component############################################')

                                latitude_path, longitude_path = new_list[i]
                                time_path = splittedTime
                                folium.Marker(new_list[i], tooltip='ini perjam', 
                                        popup=folium.Popup(popup_html_user_upload(provinsi,kab_kota,kecamatan,desa,date_component,time_component,satelit,confidence,latitude_path,longitude_path), max_width=250), 
                                        icon=dot_icon).add_to(m)
                            
                            folium.Marker(new_list[0], tooltip='Click For More Info', 
                                        popup=folium.Popup(popup_html_user_upload(provinsi,kab_kota,kecamatan,desa,splittedDate,splittedTime,satelit,confidence,latitude,longitude), max_width=250), 
                                        icon=folium.Icon(color=color, icon='fire', prefix='fa')).add_to(m)
                                
    else:
        form = HazeInitialForm()


    context = {
        'queryset': qs,
        'form' : form,
        'map' : m._repr_html_,
        'table': table,
        # 'filter': filter_table,
    }
    return render(request, 'haze_traj/haze_initial_hotspot.html', context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = HotspotSipongi.objects.all()
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    provinsi_query = request.GET.get('provinsi_filtered')
    kab_kota_query = request.GET.get('kab_kota_filtered')
    kecamatan_query = request.GET.get('kecamatan_filtered')
    desa_query = request.GET.get('desa_filtered')
        
    if is_valid_queryparam(provinsi_query):
        qs = qs.filter(nama_provinsi__icontains=provinsi_query)

    elif is_valid_queryparam(kab_kota_query):
        qs = qs.filter(kabkota__icontains=kab_kota_query)
        
    elif is_valid_queryparam(kecamatan_query):
        qs = qs.filter(kecamatan__icontains=kecamatan_query)
    
    elif is_valid_queryparam(desa_query):
        qs = qs.filter(desa__icontains=desa_query)

    if is_valid_queryparam(date_min):
        print('datemin=',date_min)
        qs = qs.filter(date_hotspot_ori__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_hotspot_ori__lt=date_max)

    return qs



# def haze_initial_hotspot(request):
#     return render (request, 'haze_traj/haze_initial_hotspot.html')

# def user_input(request):
#     return render (request, 'haze_traj/haze_user_input.html')


from django.http import HttpResponse
from .forms import InputDataForm
import pandas as pd
import matplotlib.pyplot as plt


def input_data_view(request):               #halaman haze initial user input
    m = folium.Map(zoom_start=4.5 , location=[-3.0893, 117.9213])
    if request.method == "POST": 
        form = InputDataForm(request.POST) 
        if form.is_valid(): 

            # print('lat_input:', form.cleaned_data['lat_input']) 
            print('latlong_input:', form.cleaned_data['latlong_input']) 
            print('date_input:', form.cleaned_data['date_input'])
            print('start_time_input:', form.cleaned_data['start_time_input'])
            print('altitude_input:', form.cleaned_data['altitude_input']) 
            print('runtime_input:', form.cleaned_data['runtime_input']) 

            working_dir = r'/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/working'
            storage_dir = r'/home/noval/Kuliah/App Haze/colgate'
            meteo_dir = r'/home/noval/Kuliah/App Haze/meteo'
            
            date = str(form.cleaned_data['date_input'])
            splittedDate= date.split('-')
            
            time = str(form.cleaned_data['start_time_input'])
            splittedTime= time.split(':')

            basename = 'colgate'

            years = [int(splittedDate[0])]
            months = [int(splittedDate[1])]
            hours = [int(splittedTime[0])]
            altitudes = [int(form.cleaned_data['altitude_input'])]
            
            runtime = int(form.cleaned_data['runtime_input'])
            
            list_of_coordinates = ast.literal_eval("[" + form.cleaned_data['latlong_input'] + "]")


            print('list', list_of_coordinates) 
            
            print(type(list_of_coordinates))
            
            for tpl in list_of_coordinates:
                # Access individual elements of each tuple
                lat_input = tpl[0]
                long_input = tpl[1]
                        
                location = (lat_input, long_input)
                print('locationnnn', location)
                print('1')
                
                str_coordinates=''.join(str(num).replace('.', '').replace(',', '') for num in location)
                
                filter_path=splittedDate[0]+splittedDate[1]+splittedDate[2]+splittedTime[0]+str_coordinates

                pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                                            years, months, hours, altitudes, location, runtime,
                                            monthslice=slice(int(splittedDate[2])-1, int(splittedDate[2]), 1), get_reverse=False,
                                            get_clipped=False, hysplit = "/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/exec/hyts_std")

                
                
                str_altitudes = ''.join(str(num).replace('.', '') for num in altitudes)
                #visual
                print(filter_path)
                path = '/home/noval/Kuliah/App Haze/colgate/'+'*'+str_altitudes+'*'+filter_path+'*'
                print('path is', path)
                trajgroup = pysplit.make_trajectorygroup((path))

                for traj in trajgroup[::5]:
                    line = traj.path
                    print(list(line.coords))
                    lists=list(line.coords)
                    print('list=', lists)

                    result=[]
                    for tpl in lists:
                        result.append(tpl[:2])
                            
                    new_list=[(t[1], t[0]) for t in result]        
                    print("result")
                    print(new_list)
                    print('testt')
                    
                    final_latlong=[]
                    for x, y, z in line.coords:
                        latlongs= ('({}, {})'. format(y,x,z))
                        final_latlong.append(latlongs)

                    trail_coordinates = [
                        new_list
                        ]
                    folium.PolyLine(trail_coordinates, tooltip="haze", color='red').add_to(m)
                    folium.Marker(new_list[0],
                                  popup=folium.Popup(popup_html_user_input(form.cleaned_data['date_input'],form.cleaned_data['start_time_input'],lat_input,long_input,runtime), max_width=250), 
                                  icon=folium.Icon(color='red', icon='fire', prefix='fa')).add_to(m)
                    
                    form = InputDataForm()
                

    else: 
        form = InputDataForm()
        
        
    context = {'map' : m._repr_html_,
               'form' : form,
               }
    
    return render (request, 'haze_traj/haze_user_input.html', context)


from .forms import UploadDataForm
from datetime import datetime, timedelta
from pytz import timezone, utc
from folium import plugins
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta

def upload_data_view(request):                  #halaman haze initial txt file
    m = folium.Map(height='60%', zoom_start=4.5 , location=[-3.0893, 117.9213],zoom_control=True)
    if request.method == "POST":
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file=(request.FILES["file"])
            
            altitudes = [int(form.cleaned_data['altitude_input'])]         
            runtime = int(form.cleaned_data['runtime_input'])
            basename = 'colgate'
            
            file_lines = uploaded_file.readlines()
            is_first_line = True
            for line in file_lines:
                if is_first_line:
                    is_first_line = False
                    continue
                line_data = line.decode().strip().split(',')  
                if len(line_data) == 10:  
                    provinsi = line_data[0]
                    kab_kota = line_data[1]
                    kecamatan = line_data[2]
                    desa = line_data[3]
                    str_tanggal = line_data[4]
                    str_waktu = line_data[5]
                    satelit = line_data[6]
                    confidence = line_data[7]
                    latitude = float(line_data[8])
                    longitude = float(line_data[9])
                    
                    location = (latitude, longitude)
                    
                    str_date_time_timestamps = str_tanggal +' '+ str_waktu
                    str_date_time_timestamps_partition = str_date_time_timestamps.split(' ')
                    date_part = datetime.strptime(str_date_time_timestamps_partition[0], '%d-%m-%Y')
                    time_part = datetime.strptime(str_date_time_timestamps_partition[1], '%H:%M')
                    combined_datetime_part = datetime.combine(date_part.date(), time_part.time())
                    
                    if str_date_time_timestamps_partition[2] == 'WIB':
                        tz = timezone('Asia/Jakarta')
                    elif str_date_time_timestamps_partition[2] == 'WITA':
                        tz = timezone('Asia/Makassar')
                    elif str_date_time_timestamps_partition[2] == 'WIT':
                        tz = timezone('Asia/Jayapura')
                    else:
                        tz = utc
                        
                    datetime_utc = tz.localize(combined_datetime_part).astimezone(utc)
                    
                    print('####################################################################################')
                    print(datetime_utc, 'ini datetime utc')
                    
                    date_fix = str(datetime_utc)
                    splittedDateTime= date_fix.split(' ')
                    splittedDate=splittedDateTime[0]
                    splittedTime=splittedDateTime[1]
                    #print(splittedDate)
                    print(splittedTime)
                    
                    str_splittedTime=str(splittedTime)
                    print('str split time', str_splittedTime)
                    
                    working_dir = r'/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/working'
                    storage_dir = r'/home/noval/Kuliah/App Haze/colgate'
                    meteo_dir = r'/home/noval/Kuliah/App Haze/meteo'
                    #splittedDate=splittedDateTime[0]
                    splittedDate_part= splittedDate.split('-')
                    years = [int(splittedDate_part[0])]
                    months = [int(splittedDate_part[1])]
                    
                    str_splittedTime_part= str_splittedTime.split(':')
                    hours = [int(str_splittedTime_part[0])]
                    #print('hours int', hours)
                    #print('str hours',str_splittedTime_part[0])
                    
                    
                    str_coordinates=''.join(str(num).replace('.', '').replace(',', '') for num in location)
                    #print('str coords', str_coordinates)
                
                    filter_path=splittedDate_part[0]+splittedDate_part[1]+splittedDate_part[2]+str_splittedTime_part[0]+str_coordinates

                    pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                                                years, months, hours, altitudes, location, runtime,
                                                monthslice=slice(int(splittedDate_part[2])-1, int(splittedDate_part[2]), 1), get_reverse=False,
                                                get_clipped=False, hysplit = "/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/exec/hyts_std")

                    
                    str_altitudes = ''.join(str(num).replace('.', '') for num in altitudes)
                    #visual
                    print(filter_path)
                    path = '/home/noval/Kuliah/App Haze/colgate/'+'*'+str_altitudes+'*'+filter_path+'*'
                    print('path is', path)
                    trajgroup = pysplit.make_trajectorygroup((path))
                    
                    for traj in trajgroup[::5]:
                        line = traj.path
                        # print(list(line.coords))
                        lists=list(line.coords)
                        # print('list=', lists)

                        result=[]
                        for tpl in lists:
                            result.append(tpl[:2])
                                
                        new_list=[(t[1], t[0]) for t in result]        
                        # print("result")
                        # print(new_list)
                        # print('testt')
                        
                        final_latlong=[]
                        for x, y, z in line.coords:
                            latlongs= ('({}, {})'. format(y,x,z))
                            final_latlong.append(latlongs)

                        trail_coordinates = [
                            new_list
                            ]
                        
                        if confidence == 'Low':
                            color = 'green'
                        elif confidence == 'Medium':
                            color = 'orange'
                        else:
                            color = 'red'
                        
                        folium.PolyLine(trail_coordinates, tooltip="", color=color).add_to(m)
                        
                        for i in range(1, len(new_list)):
                            dot_icon = folium.CustomIcon(
                            icon_image=f'data:image/svg+xml;utf-8,<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="{color}" /></svg>',
                            icon_size=(5, 5))
                            
                            datetime_utc += timedelta(minutes=30)
                            print(datetime_utc, 'ini stardate############################################')
                            
                            date_component = datetime_utc.date()
                            time_component = datetime_utc.time()
                            print(date_component, 'ini date_component############################################')
                            print(time_component, 'ini time_component############################################')

                            latitude_path, longitude_path = new_list[i]
                            
                            folium.Marker(new_list[i], tooltip='ini perjam', 
                                      popup=folium.Popup(popup_html_user_upload(provinsi,kab_kota,kecamatan,desa,date_component,time_component,satelit,confidence,latitude_path,longitude_path), max_width=250), 
                                      icon=dot_icon).add_to(m)
                            
                        folium.Marker(new_list[0], tooltip='Click For More Info', 
                                      popup=folium.Popup(popup_html_user_upload(provinsi,kab_kota,kecamatan,desa,splittedDate,splittedTime,satelit,confidence,latitude,longitude), max_width=250), 
                                      icon=folium.Icon(color=color, icon='fire', prefix='fa')).add_to(m)
                                      
    else:
        form = UploadDataForm()

        
    context = {'map' : m._repr_html_,
               'form' : form
               }
    #    fs = FileSystemStorage()
    #    fs.save(uploaded_file.name, uploaded_file)
    return render(request, "haze_traj/haze_user_upload.html", context)


import urllib.request

def popup_html_user_upload(provinsi,kab_kota,kecamatan,desa,tanggal,waktu,satelit,confidence,latitude,longitude):
    
    left_col_color = "#609966"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(provinsi) + """
    </head>
        <table style="height: 200px; width: 400px;">
    <tbody>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Provinsi</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(provinsi) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Kab Kota</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(kab_kota) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Kecamatan</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(kecamatan) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Desa</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(desa) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Tanggal</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(tanggal) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Waktu</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(waktu) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Satelit</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(satelit) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Confidence</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(confidence) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Latitude</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(latitude) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Longitude</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(longitude) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html

def popup_html_user_input(tanggal,waktu,latitude,longitude,runtime):
    
    left_col_color = "#609966"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:10"; width="200px">Hotspot</h4>""" """
    </head>
        <table style="height: 200px; width: 400px;">
    <tbody>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Tanggal</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(tanggal) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Waktu</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(waktu) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">latitude</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(latitude) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">longitude</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{}</td>""".format(longitude) + """
    </tr>
        <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Runtime</span></td>
    <td style="width: 170px;background-color: """+ right_col_color +""";">{} hours</td>""".format(runtime)  + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html

def ftp_test(request):
    print("1")
    urllib.request.urlretrieve('ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/hysplit/v8.0/hysplit.20230511/hysplit.t00z.gdas1f','hysplit.t00z.gdas1f')
    print("test")
