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

title = u"Железная дорога Голутвин - Озёры. График движения поездов на конец 2019\n"
title = title+"Golutvin-Ozyory. Train diagram for late 2019"

svg_filename = 'Golutvin-Ozyory-2019.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]=u"Голутвин"
stations[2]=u'Бачманово'
stations[5]=u'6 км'
stations[7]=u'Сычёво'
stations[10]=u'Лысцовская'
stations[12]=u'Семёновский'
stations[16]=u'18 км'
stations[18]=u'Карасёво'
stations[21]=u'Кудрявцево'
stations[26]=u'Даниловская'
stations[30]=u'30 км'
stations[37]=u'38 км'
stations[39]=u'Озёры'


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

trainnumbers=(6334,6336,6340,6342,6344)
trainnumbers = trainnumbers + (6335,6337,6339,6341,6343)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
    
# Type train sheldue for each train
# Date is optional


traintimes['6334'].append('2019-12-29 04:40')
stationcalls['6334'].append(0)

trainnumber='6334'
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=10)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=15)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=26)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=32)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=37)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=45)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=72)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(dateutil.parser.parse('2019-12-29 04:40')+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(39)

trainnumber='6336'
traintimes[trainnumber].append('2019-12-29 09:05')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse('2019-12-29 09:05')
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=10)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=15)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=26)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=32)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=37)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=45)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=72)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(39)

trainnumber='6340'
traintimes[trainnumber].append('2019-12-29 12:15')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse('2019-12-29 12:15')
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=10)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=15)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=26)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=32)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=37)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=45)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=72)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(39)

annotates.append({'datetime':'2019-12-29 12:15','station':2,'text':u'hollidays'})


trainnumber='6342'
traintimes[trainnumber].append('2019-12-29 17:20')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse('2019-12-29 17:20')
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=10)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=15)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=26)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=32)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=37)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=45)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=72)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(39)

trainnumber='6344'
traintimes[trainnumber].append('2019-12-29 21:05')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse('2019-12-29 21:05')
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=10)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=15)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=26)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=32)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=37)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=45)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=59)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=72)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(39)

# -------------------


trainnumber='6335'
traintimes[trainnumber].append('2019-12-29 06:15')
stationcalls[trainnumber].append(39)


frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=3)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=16)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=28)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=36)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=48)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=60)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=71)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(0)



trainnumber='6337'
traintimes[trainnumber].append('2019-12-29 10:40')
stationcalls[trainnumber].append(39)


frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=3)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=16)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=28)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=36)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=48)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=60)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=71)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(0)


trainnumber='6339'
traintimes[trainnumber].append('2019-12-29 14:10')
stationcalls[trainnumber].append(39)


frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=3)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=16)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=28)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=36)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=48)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=60)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=71)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(0)

annotates.append({'datetime':'2019-12-29 14:10','station':39,'text':u'hollidays'})


trainnumber='6341'
traintimes[trainnumber].append('2019-12-29 18:51')
stationcalls[trainnumber].append(39)


frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=3)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=16)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=28)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=36)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=48)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=60)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=71)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(0)


trainnumber='6343'
traintimes[trainnumber].append('2019-12-29 22:37')
stationcalls[trainnumber].append(39)


frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=3)))
stationcalls[trainnumber].append(37)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=16)))
stationcalls[trainnumber].append(30)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(26)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=28)))
stationcalls[trainnumber].append(21)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=36)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(16)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=48)))
stationcalls[trainnumber].append(12)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=53)))
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=60)))
stationcalls[trainnumber].append(7)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=65)))
stationcalls[trainnumber].append(5)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=71)))
stationcalls[trainnumber].append(2)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=77)))
stationcalls[trainnumber].append(0)


'''
stations[12]=u'Семёновский'
stations[16]=u'18 км'
stations[18]=u'Карасёво'
stations[21]=u'Кудрявцево'
stations[26]=u'Даниловская'
stations[30]=u'30 км'
stations[37]=u'38 км'
stations[39]=u'Озёры'
'''

# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1

horizontal_axis_label_format='%d %H:%M'

x_bounds = [datetime.datetime(2019, 12, 29,4,40), datetime.datetime(2019, 12, 29,23,55)]

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