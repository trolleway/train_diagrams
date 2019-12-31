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

title = u"Курское направление. График движения дальних поездов на конец 2019\n"
title = title+"Moskva-Kurskaya-Serpukhov. Train diagram for late 2019"

svg_filename = 'Moskva-Kurskaya-Serpukhov-2019.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]=u"Москва"
stations[13]=u"Перерва"
stations[18]=u"Царицыно"
stations[33]=u"Щербинка"
stations[42]=u"Подольск"
stations[51]=u"Гривно"
stations[56]=u"Львовская"
stations[63]=u"Столбовая"
stations[74]=u"Чехов"
stations[86]=u"Шарапова Охота"
stations[98]=u"Серпухов"
stations[193]=u"Тула-расчёт"




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

trainnumbers=(119,143,479,109,'057',6414,6416,6418,6420)
trainnumbers = trainnumbers + (6401,6403,6405,6407,6409,6411,6413,6415,6417,6419)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
    
# Type train sheldue for each train
# Date is optional



trainnumber='119'
traintimes[trainnumber].append('2019-12-29 09:47')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=18)))
stationcalls[trainnumber].append(13)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=25)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(33)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=51)))
stationcalls[trainnumber].append(42)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=61)))
stationcalls[trainnumber].append(51)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=6)))
stationcalls[trainnumber].append(56)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16)))
stationcalls[trainnumber].append(63)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9)))
stationcalls[trainnumber].append(74)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9+7)))
stationcalls[trainnumber].append(86)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=100)))
stationcalls[trainnumber].append(98)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=167)))
stationcalls[trainnumber].append(193)

#annotates.append({'datetime':'2019-12-29 09:47','station':0,'text':u'Ежедневно'})

trainnumber='143'
traintimes[trainnumber].append('2019-12-29 09:56')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=18)))
stationcalls[trainnumber].append(13)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=25)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(33)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=51)))
stationcalls[trainnumber].append(42)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=61)))
stationcalls[trainnumber].append(51)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=6)))
stationcalls[trainnumber].append(56)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16)))
stationcalls[trainnumber].append(63)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9)))
stationcalls[trainnumber].append(74)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9+7)))
stationcalls[trainnumber].append(86)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=100)))
stationcalls[trainnumber].append(98)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=167)))
stationcalls[trainnumber].append(193)

annotates.append({'datetime':'2019-12-29 09:56','station':0,'text':u'Летом по дням'})


trainnumber='479'
traintimes[trainnumber].append('2019-12-29 10:35')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=18)))
stationcalls[trainnumber].append(13)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=25)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(33)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=51)))
stationcalls[trainnumber].append(42)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=61)))
stationcalls[trainnumber].append(51)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=6)))
stationcalls[trainnumber].append(56)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16)))
stationcalls[trainnumber].append(63)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9)))
stationcalls[trainnumber].append(74)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9+7)))
stationcalls[trainnumber].append(86)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=100)))
stationcalls[trainnumber].append(98)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=167)))
stationcalls[trainnumber].append(193)

annotates.append({'datetime':'2019-12-29 11:00','station':18,'text':u'Летом по дням'})


trainnumber='109'
traintimes[trainnumber].append('2019-12-29 19:58')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=18)))
stationcalls[trainnumber].append(13)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=25)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(33)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=51)))
stationcalls[trainnumber].append(42)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=61)))
stationcalls[trainnumber].append(51)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=6)))
stationcalls[trainnumber].append(56)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16)))
stationcalls[trainnumber].append(63)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9)))
stationcalls[trainnumber].append(74)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9+7)))
stationcalls[trainnumber].append(86)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=100)))
stationcalls[trainnumber].append(98)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=167)))
stationcalls[trainnumber].append(193)

annotates.append({'datetime':'2019-12-29 19:58','station':0,'text':u'По дням'})


trainnumber='057'
traintimes[trainnumber].append('2019-12-29 20:58')
stationcalls[trainnumber].append(0)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=18)))
stationcalls[trainnumber].append(13)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=25)))
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=41)))
stationcalls[trainnumber].append(33)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=51)))
stationcalls[trainnumber].append(42)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=61)))
stationcalls[trainnumber].append(51)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=6)))
stationcalls[trainnumber].append(56)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16)))
stationcalls[trainnumber].append(63)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9)))
stationcalls[trainnumber].append(74)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(hours=1,minutes=16+9+7)))
stationcalls[trainnumber].append(86)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=100)))
stationcalls[trainnumber].append(98)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=167)))
stationcalls[trainnumber].append(193)






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


#ax.set_xlim(x_bounds)

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