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

title = u"Сахалинская железная дорога. Западная линия. График движения поездов на 2022 \n"
title = title+"Sakhalin railway, West coast line. Train diagram for 2022. Local time "

svg_filename = 'Sakhalin railway train diagram west 2022.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

#https://transsib.ru/large-st.htm

stations=dict()
stations[75]="Чёртов мост /75 км ПК6"
stations[87]="Холмск"
stations[90]="Холмск-Северный"
stations[104]="Чехов-Сахалинский"
stations[146]="Томари"
stations[179]="Ильинск-Сахалинский"

# You can get kilometers from OpenStreetMap under open license at
#http://brouter.de/brouter-web/#map=10/55.5838/37.2927/standard,HikeBike.HillShading&lonlats=37.581269,55.777273;36.881192,55.700614&profile=rail


#transliterate station names
#may be replaced to load dataset with official latin names
from transliterate import translit, get_available_language_codes
for id in stations:
    if ' км' in stations[id]: continue
    stations[id] = stations[id]+"\n"+translit(stations[id], 'ru',reversed=True)
    stations[id] = stations[id]+" "+str(id)+' km'



# Timezones
# In most cases, you do not need to use timezones, type times in local time
# If line is so long as Baikal-Amur mainline,
# type times in standart time (Moscow), and type timedelta here (Moscow + 6 hours)

#TIMEZONE is MSK
time_add = datetime.timedelta(hours=0)

# Type train numbers or IDs here.
# numbers can be numeric or string, and converted to string later.

trainnumbers = list()
# Type train sheldue for each train
# Date is optional
# Local time

#weekdays




trainnumber='6101'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 05:34')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 06:43')
stationcalls[trainnumber].append(104)#Чехов
annotates.append({'datetime':'2022-08-01 06:10','station':95,'text':'Tue, We, Thursday, Sunday'})


trainnumber='6102'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 06:53')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 08:20')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 08:22')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 08:50')
stationcalls[trainnumber].append(75)#Чёртов
traintimes[trainnumber].append('2022-08-01 09:10')
stationcalls[trainnumber].append(75)#Чёртов
traintimes[trainnumber].append('2022-08-01 09:40')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 09:49')
stationcalls[trainnumber].append(90)#Холмск
annotates.append({'datetime':'2022-08-01 07:10','station':100,'text':'Every day'})

trainnumber='6103'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 13:24')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 14:53')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 15:03')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 16:32')
stationcalls[trainnumber].append(87)#Чехов
traintimes[trainnumber].append('2022-08-01 17:00')
stationcalls[trainnumber].append(75)#Чёртов


trainnumber='6105'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 17:16')
stationcalls[trainnumber].append(75)#Чёртов
traintimes[trainnumber].append('2022-08-01 17:45')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 17:50')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 19:16')
stationcalls[trainnumber].append(104)#Чехов


trainnumber='6106'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 19:26')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 20:47')
stationcalls[trainnumber].append(87)#Холмск

annotates.append({'datetime':'2022-08-01 19:26','station':104,'text':'Tue, We, Thursday, Sunday'})

trainnumber='6107'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 03:43')
stationcalls[trainnumber].append(87)#Холмск
traintimes[trainnumber].append('2022-08-01 04:53')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 05:44')
stationcalls[trainnumber].append(146)#Томари
annotates.append({'datetime':'2022-08-01 04:53','station':104,'text':'Monday, Friday, Saturday'})


trainnumber='6108'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 05:54')
stationcalls[trainnumber].append(146)#Томари
traintimes[trainnumber].append('2022-08-01 06:53')
stationcalls[trainnumber].append(104)#Чехов
#traintimes[trainnumber].append('2022-08-01 08:20')

annotates.append({'datetime':'2022-08-01 06:35','station':120,'text':'Monday, Friday, Saturday'})

trainnumber='6109'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 19:19')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 20:14')
stationcalls[trainnumber].append(146)#Томари
annotates.append({'datetime':'2022-08-01 19:59','station':140,'text':'Monday, Friday, Saturday'})

trainnumber='6110'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 20:24')
stationcalls[trainnumber].append(146)#Томари
traintimes[trainnumber].append('2022-08-01 21:17')
stationcalls[trainnumber].append(104)#Чехов
traintimes[trainnumber].append('2022-08-01 22:37')
stationcalls[trainnumber].append(87)#Холмск

annotates.append({'datetime':'2022-08-01 21:00','station':120,'text':'Monday, Friday, Saturday'})

trainnumber='6203'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 04:11')
stationcalls[trainnumber].append(146)#Томари
traintimes[trainnumber].append('2022-08-01 04:54')
stationcalls[trainnumber].append(179)#Ильинск
traintimes[trainnumber].append('2022-08-01 05:04')
stationcalls[trainnumber].append(179)#Ильинск

annotates.append({'datetime':'2022-08-01 05:05','station':179,'text':'To Uyzhno-Sakhalinsk every day'})

trainnumber='6202'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 20:29')
stationcalls[trainnumber].append(179)#Ильинск
traintimes[trainnumber].append('2022-08-01 20:39')
stationcalls[trainnumber].append(179)#Ильинск
traintimes[trainnumber].append('2022-08-01 21:24')
stationcalls[trainnumber].append(146)#Томари

annotates.append({'datetime':'2022-08-01 20:29','station':179,'text':'From Uyzhno-Sakhalinsk every day'})


'''
stations[75]="Чёртов мост /75 км ПК6"
stations[87]="Холмск"
stations[90]="Холмск-Северный"
stations[104]="Чехов-Сахалинский"
stations[146]="Томари"
stations[179]="Ильинск-Сахалинский"
'''





# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1
train_color = '#b10026'
horizontal_axis_label_format='%H'

# Time bounds of figure
x_bounds = [datetime.datetime(2022, 8, 1,3,0), datetime.datetime(2022, 8, 1,23,5)]
#Size of figure
figsize=(19,9)

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
    ax.plot(traintimes[trainnumber],stationcalls[trainnumber],train_line_style,label=trainnumber, color = train_color, antialiased=True)
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
plt.tight_layout()
plt.savefig(svg_filename)
plt.show()
