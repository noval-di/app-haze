from django.shortcuts import render
from .models import Haze_traj
import pysplit
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
import ast

# Create your views here.

def index(request):
    return render (request, 'haze_traj/index.html')

def about(request):
    
    haze_trajs= Haze_traj.objects.all()[:5]
    context={
        'haze_trajs': haze_trajs
    }
    return render (request, 'haze_traj/about.html',context)

def haze_initial_hotspot(request):
    return render (request, 'haze_traj/haze_initial_hotspot.html')

def user_input(request):
    return render (request, 'haze_traj/haze_user_input.html')


from django.http import HttpResponse
from .forms import InputDataForm
from .forms import InputDataForm_backup
import pandas as pd
import matplotlib.pyplot as plt

# def input_data_view(request):
#     m = folium.Map(zoom_start=4.5 , location=[-3.0893, 117.9213])
#     if request.method == "POST": 
#         form = InputDataForm(request.POST) 
#         if form.is_valid(): 

#             print('lat_input:', form.cleaned_data['lat_input']) 
#             print('long_input:', form.cleaned_data['long_input']) 
#             print('date_input:', form.cleaned_data['date_input'])
#             print('start_time_input:', form.cleaned_data['start_time_input'])
#             print('altitude_input:', form.cleaned_data['altitude_input']) 
#             print('runtime_input:', form.cleaned_data['runtime_input']) 

#             working_dir = r'/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/working'
#             storage_dir = r'/home/noval/Kuliah/App Haze/colgate'
#             meteo_dir = r'/home/noval/Kuliah/App Haze/meteo'
            
#             date = str(form.cleaned_data['date_input'])
#             splittedDate= date.split('-')
            
#             time = str(form.cleaned_data['start_time_input'])
#             splittedTime= time.split(':')

#             basename = 'colgate'

#             years = [int(splittedDate[0])]
#             months = [int(splittedDate[1])]
#             hours = [int(splittedTime[0])]
#             altitudes = [int(form.cleaned_data['altitude_input'])]
#             location = (form.cleaned_data['lat_input'], form.cleaned_data['long_input'])
#             runtime = int(form.cleaned_data['runtime_input'])
            
#             print('1')
            
#             str_coordinates=''.join(str(num).replace('.', '').replace(',', '') for num in location)
            
#             filter_path=splittedDate[0]+splittedDate[1]+splittedDate[2]+splittedTime[0]+str_coordinates

#             pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                                         years, months, hours, altitudes, location, runtime,
#                                         monthslice=slice(int(splittedDate[2])-1, int(splittedDate[2]), 1), get_reverse=False,
#                                         get_clipped=False, hysplit = "/home/noval/Downloads/hysplit.v5.2.3_UbuntuOS20.04.4LTS/exec/hyts_std")

            
            
#             str_altitudes = ''.join(str(num).replace('.', '') for num in altitudes)
#             #visual
#             print(filter_path)
#             path = '/home/noval/Kuliah/App Haze/colgate/'+'*'+str_altitudes+'*'+filter_path+'*'
#             print('path is', path)
#             trajgroup = pysplit.make_trajectorygroup((path))
            
#             # mapcorners =  [-268, -8, -240, 6]
#             # standard_pm = None

#             # bmap_params = pysplit.MapDesign(mapcorners, standard_pm)

#             # bmap = bmap_params.make_basemap()

#             # color_dict = {500.0 : 'blue',
#             #             1000.0 : 'orange',
#             #             1500.0 : 'black',
#             #             1234.0: 'purple'}
            
#             # for traj in trajgroup:
#             #     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#             #     traj.trajcolor = color_dict[altitude0]
#             #     print(traj)
            
#             # print('123')
#             # print(traj)
#             # print('456')

#             for traj in trajgroup[::5]:
#                 #ret= bmap.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20)
                
#                 # print(traj.path)
#                 line = traj.path
#                 # line.coords
#                 print(list(line.coords))
#                 lists=list(line.coords)
#                 print('list=', lists)

#                 result=[]
#                 for tpl in lists:
#                     result.append(tpl[:2])
                        
#                 new_list=[(t[1], t[0]) for t in result]        
#                 print("result")
#                 print(new_list)

                
                
#                 # list_coor= [i[(n, n+1)] for i in list(line.coords)]
#                 # print(list_coor)
#                 # data_xy = [(x,y) for x,y,z in list_coor]
#                 # print(data_xy)
#                 print('testt')
                
#                 final_latlong=[]
#                 for x, y, z in line.coords:
#                     latlongs= ('({}, {})'. format(y,x,z))
#                     final_latlong.append(latlongs)
#                     # xyz= line.coords.xyz
#                     # longs= xyz[0].tolist()
#                     # lats= xyz[1].tolist()
                    
#                     #print('({}, {})'. format(y,x,z))

#                 # x,y,z = line.coords.xyz
#                 # pd.DataFrame(list(zip(x,y)), columns=['LAT', 'LON'])

#                 #print(final_latlong)
#                 #print(ret)
                
#                 #date = str(form.cleaned_data['date_input'])
#                 #splittedDate= date.split('-')
                
#                 #date = str(form.cleaned_data['date_input'])
#                 #splittedTraj= traj.path.split(',')
#                 #print(splittedTraj)
                
                
#                 trail_coordinates = [
#                     new_list
#                     ]
#                 folium.PolyLine(trail_coordinates, tooltip="haze", color='red').add_to(m)
                
#                 form = InputDataForm()
                
#                 #plt.show()
                
#                 #return HttpResponse("data is submitted") 
#     else: 
#         form = InputDataForm()
        
        
#     context = {'map' : m._repr_html_,
#                'form' : form
#                }
    
#     return render (request, 'haze_traj/haze_user_input.html', context)



def input_data_view(request):
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
               'form' : form
               }
    
    return render (request, 'haze_traj/haze_user_input.html', context)


def input_data_view_2(request):
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
                print(splittedTime[0])

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
                    folium.Marker(new_list[0], tooltip='Click For More Info',
                                  popup=folium.Popup(popup_html_user_input(form.cleaned_data['date_input'],form.cleaned_data['start_time_input'],lat_input,long_input,runtime), max_width=250), 
                                  icon=folium.Icon(color='red', icon='fire', prefix='fa')).add_to(m)
                    
                    form = InputDataForm()
                
                

    else: 
        form = InputDataForm()
        
        
    context = {'map' : m._repr_html_,
               'form' : form
               }
    
    return render (request, 'haze_traj/haze_initial_hotspot.html', context)


    
def popup_html_user_input(tanggal,waktu,latitude,longitude,runtime):
    
    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(runtime) + """
    </head>
        <table style="height: 126px; width: 350px;">
    <tbody>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Tanggal</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(tanggal) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Waktu</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(waktu) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">latitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(latitude) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">longitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(longitude) + """
    </tr>
        <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Runtime</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(runtime) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html
######################################################################

######################################################################

from .forms import UploadDataForm

from datetime import datetime, timedelta
from pytz import timezone, utc
from folium import plugins

from django.core.files.storage import FileSystemStorage

def upload_data_view(request):
    m = folium.Map(zoom_start=4.5 , location=[-3.0893, 117.9213])
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
                    
                    #print(datetime_utc)
                    
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
                    print('hours int', hours)
                    print('str hours',str_splittedTime_part[0])
                    
                    
                    str_coordinates=''.join(str(num).replace('.', '').replace(',', '') for num in location)
                    print('str coords', str_coordinates)
                
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
                        elif confidence == 'Medium':
                            color = 'orange'
                        else:
                            color = 'red'
                            
                        labels= 'testest'
                        
                        folium.PolyLine(trail_coordinates, tooltip="haze", color=color).add_to(m)
                        
                        folium.Marker(new_list[0], tooltip='Click For More Info', 
                                      popup=folium.Popup(popup_html_user_upload(provinsi,kab_kota,kecamatan,desa,splittedDate,splittedTime,satelit,confidence,latitude,longitude), max_width=250), 
                                      icon=folium.Icon(color=color, icon='fire', prefix='fa')).add_to(m)
                        
                        # polyline.add_child(marker)
                        # map_html = m.get_root().render()

                        # Enable ClickForMarker plugin
                        
                        
                        
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
    
    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(provinsi) + """
    </head>
        <table style="height: 126px; width: 350px;">
    <tbody>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Provinsi</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(provinsi) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Kab Kota</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(kab_kota) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Kecamatan</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(kecamatan) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Desa</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(desa) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Tanggal</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(tanggal) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Waktu</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(waktu) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Satelit</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(satelit) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Confidence</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(confidence) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">latitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(latitude) + """
    </tr>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">longitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(longitude) + """
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
