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
import dateutil 



# Template code for generation of train sheldue diagram
# Copy this file, and type in your times

# data sample
traintimes=dict()
stationcalls=dict()
annotates=list()

# Type graph label here

title = u"Лыжный поезд Яхрома. График движения 2021\n"
title = title+"Yahroma ski train. Train diagram 2021"

svg_filename = 'Yahroma ski train. Train diagram 2021.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]=u"Савёловская"
stations[3]=u"Окружная"
stations[53]=u'Турист'
stations[58]=u'Яхрома'


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

trainnumbers=(7092,7094,6180,6706,6708,6710)
trainnumbers = trainnumbers + (7091,7093,6705,6707,6709)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
    
# Type train sheldue for each train
# Date is optional
# Local time


# Optionaly set times as delta from prev station
trainnumber='7092'
traintimes[trainnumber].append('2021-01-17 08:16')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=57)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(58)

trainnumber='7094'
traintimes[trainnumber].append('2021-01-17 15:46')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=57)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(58)

trainnumber='6180'
traintimes[trainnumber].append('2021-01-17 12:31')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])

traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=82)))
stationcalls[trainnumber].append(58)



# Optionaly set annotates 
annotates.append({'datetime':'2021-01-17 09:20','station':58,'text':u'Ski'})
annotates.append({'datetime':'2021-01-17 14:06','station':58,'text':u'Ski'})
annotates.append({'datetime':'2021-01-17 17:02','station':58,'text':u'Ski'})
annotates.append({'datetime':'2021-01-17 21:28','station':58,'text':u'Ski'})

annotates.append({'datetime':'2021-01-17 13:33','station':40,'text':u'Звенигород-Дмитров'})



annotates.append({'datetime':'2021-01-17 09:00','station':0,'text':u'daylight 16.01'})
annotates.append({'datetime':'2021-01-17 16:21','station':0,'text':u'sunset 16.01'})

annotates.append({'datetime':'2021-01-17 07:41','station':0,'text':u'daylight 23.02'})
annotates.append({'datetime':'2021-01-17 17:48','station':0,'text':u'sunset 23.02'})

#-------down trains ---------------
'''
stations[0]=u"Торфяная"
stations[3]=u'Новый'
stations[4]=u'Вернисаж'
stations[5]=u'Боёво'
stations[6]=u'Мост через Чепцу'
stations[8]=u'Пойма'
stations[10]=u'Бор'
stations[13]=u'Техническая (Каринторф)'
'''

trainnumber='7091'
traintimes[trainnumber].append('2021-01-17 14:06')
stationcalls[trainnumber].append(58)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=62)))
stationcalls[trainnumber].append(6)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=63)))
stationcalls[trainnumber].append(6)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=64)))
stationcalls[trainnumber].append(0)


trainnumber='7093'
traintimes[trainnumber].append('2021-01-17 21:28')
stationcalls[trainnumber].append(58)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=62)))
stationcalls[trainnumber].append(6)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=63)))
stationcalls[trainnumber].append(6)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=64)))
stationcalls[trainnumber].append(0)




trainnumber='6705'
traintimes[trainnumber].append('2020-06-01 13:20')
stationcalls[trainnumber].append(13)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(8)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=29)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=34)))
stationcalls[trainnumber].append(4)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=40)))
stationcalls[trainnumber].append(3)

trainnumber='6707'
traintimes[trainnumber].append('2020-06-01 16:40')
stationcalls[trainnumber].append(13)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(8)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=29)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=34)))
stationcalls[trainnumber].append(4)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=40)))
stationcalls[trainnumber].append(3)

trainnumber='6709'
traintimes[trainnumber].append('2020-06-01 19:15')
stationcalls[trainnumber].append(13)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(8)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24))) #этот поезд почему-то быстрее
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=29)))
stationcalls[trainnumber].append(4)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=35)))
stationcalls[trainnumber].append(3)



# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1

horizontal_axis_label_format='%d %H:%M'

x_bounds = [dateutil.parser.parse('2021-01-17 07:30'), dateutil.parser.parse('2021-01-17 23:00')]

figsize=(18,9)

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