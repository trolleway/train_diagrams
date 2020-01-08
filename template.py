#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import dateutil
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
                               
import datetime



# Template code for generation of train sheldue diagram
# Copy this file, and type in your times

# data sample
traintimes=dict()
stationcalls=dict()
annotates=list()

# Type graph label here

title = u"Звенигородская ветка. График движения поездов на конец 2019\n"
title = title+"Zvenigorod branch. Train diagram for late 2019"

svg_filename = 'template test graph.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]=u"Москва-Смоленская"
stations[43]=u'Голицыно'
stations[48]=u'Захарово'
stations[51]=u'Хлюпино'
stations[55]=u'Скоротово'
stations[59]=u'Звенигород'

# You can get kilometers from OpenStreetMap under open license at 
#http://brouter.de/brouter-web/#map=10/55.5838/37.2927/standard,HikeBike.HillShading&lonlats=37.581269,55.777273;36.881192,55.700614&profile=rail


#transliterate station names
#may be replaced to load dataset with official latin names
from transliterate import translit, get_available_language_codes
for id in stations:
    stations[id] = stations[id]+"\n"+translit(stations[id], 'ru',reversed=True)



# Timezones
# In most cases, you do not need to use timezones, type local time
# If line is so long as Baikal-Amur mainline, 
# type times in standart time (Moscow), and type timedelta here (Moscow + 6 hours)

#TIMEZONE is MSK
time_add = datetime.timedelta(hours=0)

# Type train numbers or IDs here. 
# numbers can be numeric or string, and converted to string later.

trainnumbers=(6405,6103,6111,6121,6131,6135,6401,6155,6165,6173,6183,7457,6209,7461,6403,7463,6231)
trainnumbers = trainnumbers + (6144,6150,6158,6164,6408,6186,6410,7464,6412,6414)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
    
# Type train sheldue for each train
# Date is optional
# Local time

trainnumber='6183'
traintimes[trainnumber].append('2020-06-01 16:18')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2020-06-01 17:20')
stationcalls[trainnumber].append(43)
traintimes[trainnumber].append('2020-06-01 17:41')
stationcalls[trainnumber].append(59)

traintimes['7457'].append('2020-06-01 17:57')
stationcalls['7457'].append(0)
traintimes['7457'].append('2020-06-01 18:42')
stationcalls['7457'].append(43)
traintimes['7457'].append('2020-06-01 18:59')
stationcalls['7457'].append(59)

# Optionaly set times as delta from prev station
trainnumber='6401'
traintimes[trainnumber].append('2020-06-01 17:00')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=78)))
stationcalls[trainnumber].append(43)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=88)))
stationcalls[trainnumber].append(55)

# Optionaly set annotates 
annotates.append({'datetime':'2020-06-01 17:00','station':0,'text':u'hollidays'})

#-------down trains ---------------


traintimes['6410'].append('2020-06-01 17:54')
stationcalls['6410'].append(59)
traintimes['6410'].append('2020-06-01 18:18')
stationcalls['6410'].append(43)
traintimes['6410'].append('2020-06-01 19:13')
stationcalls['6410'].append(0)

traintimes['7464'].append('2020-06-01 19:14')
stationcalls['7464'].append(59)
traintimes['7464'].append('2020-06-01 19:34')
stationcalls['7464'].append(43)
traintimes['7464'].append('2020-06-01 20:23')
stationcalls['7464'].append(0)

# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1

horizontal_axis_label_format='%d %H:%M'

x_bounds = [datetime.datetime(2020, 06, 01,07,00), datetime.datetime(2020, 06, 01,20)]

figsize=(9,9)

# END OF STYLING



def convert_dates(times_list):
    n = list()
    for i in times_list:
        temp_dt = dateutil.parser.parse(str(i)) + time_add
        n.append(temp_dt)


    return(n)

for k in traintimes:
    temp_dict=dict()
    temp_dict=convert_dates(traintimes[k])
    traintimes[k] = temp_dict
   
fig, ax = plt.subplots(figsize=figsize)


# styling

hours = mdates.HourLocator(interval=vertical_hour_ticks_interval) 
hours_fmt = mdates.DateFormatter(horizontal_axis_label_format)  
plt.title(title)

# station labels generate
station_names=list()
station_pks=list()
for elem in sorted(stations.items()) :
    print(elem[0] , " ::" , elem[1] )
    station_names.append(elem[1])
    station_pks.append(elem[0])
    

plt.yticks(station_pks)
ax.set_yticklabels(station_names)


ax.set_xlim(x_bounds)

for trainnumber in traintimes:
    print(trainnumber)
    ax.plot(traintimes[trainnumber],stationcalls[trainnumber],train_line_style,label=trainnumber, color = 'gray', antialiased=False)
    #ax.set_ylabel(r'stations')
    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(hours_fmt)

    plt.gcf().autofmt_xdate()
    ax.grid(True)
	
#Annotates
if len(annotates) > 0:
    for annotate in annotates:
        ax.annotate(annotate['text'], (mdates.date2num(dateutil.parser.parse(str(annotate['datetime']))), annotate['station']), xytext=(15, 15), 
            textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))	
    
#plt.legend(title='Trains:')
plt.savefig(svg_filename)
plt.show()