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

title = u"Сахалинская железная дорога. Восточная линия. График движения поездов на 2022 \n"
title = title+"Sakhalin railway, East coast line. Train diagram for 2022. Local time "

svg_filename = 'Sakhalin railway train diagram 2022.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

#https://transsib.ru/large-st.htm

stations=dict()
stations[0]="Корсаков - Пять Углов"
stations[40]="Южно-Сахалинск"
stations[83]="Долинск"
stations[157]="Арсентьевка"
stations[328]="Поронайск"
stations[410]="Победино"
stations[651]="Ноглики"

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


trainnumber='603'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 20:07')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-02 02:12')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-02 02:32')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-02 08:46')
stationcalls[trainnumber].append(651) #Ноглики
traintimes[trainnumber].append('2022-08-02 18:16')
stationcalls[trainnumber].append(651) #Ноглики
traintimes[trainnumber].append('2022-08-03 00:32')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-03 00:52')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-03 06:50')
stationcalls[trainnumber].append(40) #Южно-Сахалинск

trainnumber='603_02'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 20:07')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-03 02:12')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-03 02:32')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-03 08:46')
stationcalls[trainnumber].append(651) #Ноглики
traintimes[trainnumber].append('2022-08-03 18:16')
stationcalls[trainnumber].append(651) #Ноглики
traintimes[trainnumber].append('2022-08-04 00:32')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-04 00:52')
stationcalls[trainnumber].append(328) #Поронайск
traintimes[trainnumber].append('2022-08-04 06:50')
stationcalls[trainnumber].append(40) #Южно-Сахалинск



trainnumber='6301-6302'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 08:15')
stationcalls[trainnumber].append(328)
traintimes[trainnumber].append('2022-08-02 10:41')
stationcalls[trainnumber].append(410) #Победино
traintimes[trainnumber].append('2022-08-02 16:22')
stationcalls[trainnumber].append(410) #Победино
traintimes[trainnumber].append('2022-08-02 18:47')
stationcalls[trainnumber].append(328)


trainnumber='6304'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 16:00')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-01 20:57')
stationcalls[trainnumber].append(328)


trainnumber='6304-2'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 16:00')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-02 20:57')
stationcalls[trainnumber].append(328)

trainnumber='poronaisk-sakhalinsk'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 05:49')
stationcalls[trainnumber].append(328)
traintimes[trainnumber].append('2022-08-02 10:47')
stationcalls[trainnumber].append(40)


trainnumber='6201-6202'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-01 17:35')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-01 19:54')
stationcalls[trainnumber].append(157)

trainnumber='6202-6201'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 05:40')
stationcalls[trainnumber].append(157)
traintimes[trainnumber].append('2022-08-02 08:00')
stationcalls[trainnumber].append(40)


trainnumber='6201-6202-02'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 17:35')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-02 19:54')
stationcalls[trainnumber].append(157)

trainnumber='6202-6201-02'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-03 05:40')
stationcalls[trainnumber].append(157)
traintimes[trainnumber].append('2022-08-03 08:00')
stationcalls[trainnumber].append(40)



trainnumber='6404-r'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 09:15')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-02 10:13')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 10:23')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 11:25')
stationcalls[trainnumber].append(40)
annotates.append({'datetime':'2022-08-02 10:13','station':0,'text':'Saturday'})


trainnumber='6402-r'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 13:15')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-02 14:13')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 14:23')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 15:35')
stationcalls[trainnumber].append(40)
annotates.append({'datetime':'2022-08-02 14:13','station':0,'text':'Friday'})

trainnumber='6016-r'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 18:30')
stationcalls[trainnumber].append(40)
traintimes[trainnumber].append('2022-08-02 19:43')
stationcalls[trainnumber].append(0)
annotates.append({'datetime':'2022-08-02 18:30','station':40,'text':'except Sat'})

trainnumber='6015'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 20:17')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 21:29')
stationcalls[trainnumber].append(40)
annotates.append({'datetime':'2022-08-02 20:17','station':5,'text':'except sat, mon'})


trainnumber='6405'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 20:26')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 21:29')
stationcalls[trainnumber].append(40)



trainnumber='6407'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-08-02 21:32')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-08-02 22:36')
stationcalls[trainnumber].append(40)
annotates.append({'datetime':'2022-08-02 22:36','station':40,'text':'monday'})

'''
original_number = trainnumber
trainnumber='603_02'
trainnumbers.append(trainnumber)
for i in stationcalls[original_number]:
    stationcalls[trainnumber]=stationcalls[original_number]

for i in traintimes[original_number]:
    traintimes[trainnumber]=traintimes[original_number].replace('-08-01')
'''
annotates.append({'datetime':'2022-08-02 19:53','station':157,'text':u'to Tomari via West Coast line'})


# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1
train_color = '#b10026'
horizontal_axis_label_format='%H'

# Time bounds of figure
x_bounds = [datetime.datetime(2022, 8, 1,15,0), datetime.datetime(2022, 8, 3,11,5)]
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
