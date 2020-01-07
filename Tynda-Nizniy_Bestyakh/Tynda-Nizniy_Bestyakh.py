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

title = u"Тында - Нижний Бестях. График движения поездов на 2020\n"
title = title+"Tynda-Nizniy_Bestyakh. Train diagram for 2020"

svg_filename = 'Tynda-Nizniy_Bestyakh.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]=u"Тында"
stations[227]=u'Нерюнгри'
stations[586]=u'Томмот'
stations[1022]=u'Нижний Бестях'


# You can get kilometers from OpenStreetMap under open license at 
#http://brouter.de/brouter-web/#map=10/55.5838/37.2927/standard,HikeBike.HillShading&lonlats=37.581269,55.777273;36.881192,55.700614&profile=rail


#transliterate station names
#may be replaced to load dataset with official latin names
from transliterate import translit, get_available_language_codes
for id in stations:
    stations[id] = stations[id]+"\n"+translit(stations[id], 'ru',reversed=True)



# Timezones
# In most cases, you do not need to use timezones, type times in local time
# If line is so long as Baikal-Amur mainline, 
# type times in standart time (Moscow), and type timedelta here (Moscow + 6 hours)

#TIMEZONE is MSK
time_add = datetime.timedelta(hours=0)

# Type train numbers or IDs here. 
# numbers can be numeric or string, and converted to string later.

trainnumbers=(325,687,376,324,328)
trainnumbers = trainnumbers + (375,325,'687b',6164,6408,6186,6410,7464,6412,6414)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
    
# Type train sheldue for each train
# Date is optional
# Local time

trainnumber='325'
traintimes[trainnumber].append('2020-02-01 02:00')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2020-02-01 07:26')
stationcalls[trainnumber].append(227)

# Optionaly set annotates 
annotates.append({'datetime':'2020-02-01 02:00','station':0,'text':u'Каждый день\nevery day'})

trainnumber='687'
traintimes[trainnumber].append('2020-02-01 10:16')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2020-02-01 15:16')
stationcalls[trainnumber].append(227)

annotates.append({'datetime':'2020-02-01 10:16','station':0,'text':u'По дням\nSome days'})

trainnumber='376'
traintimes[trainnumber].append('2020-02-01 18:10')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2020-02-01 23:27')
stationcalls[trainnumber].append(227)

annotates.append({'datetime':'2020-02-01 18:10','station':0,'text':u'По дням\nSome days'})

#nerungru-tommot
trainnumber='324'
traintimes[trainnumber].append('2020-02-01 09:20')
stationcalls[trainnumber].append(227)
traintimes[trainnumber].append('2020-02-01 17:25')
stationcalls[trainnumber].append(586)

annotates.append({'datetime':'2020-02-01 09:20','station':227,'text':u'Каждый день\nevery day'})


#tommot-nizniy_bestyakh
trainnumber='328'
traintimes[trainnumber].append('2020-02-01 19:00')
stationcalls[trainnumber].append(586)
traintimes[trainnumber].append('2020-02-02 05:02')
stationcalls[trainnumber].append(1022)

annotates.append({'datetime':'2020-02-01 19:00','station':586,'text':u'По дням\nSome days'})



# down trains
'''

trainnumber='375'
traintimes[trainnumber].append('2020-02-01 06:10')
stationcalls[trainnumber].append(227)
traintimes[trainnumber].append('2020-02-01 11:26')
stationcalls[trainnumber].append(0)

# Optionaly set annotates 
annotates.append({'datetime':'2020-02-01 11:26','station':0,'text':u'odd days'})

trainnumber='687b'
traintimes[trainnumber].append('2020-02-01 18:01')
stationcalls[trainnumber].append(227)
traintimes[trainnumber].append('2020-02-01 23:05')
stationcalls[trainnumber].append(0)

annotates.append({'datetime':'2020-02-01 23:05','station':0,'text':u'even days'})

trainnumber='325'
traintimes[trainnumber].append('2020-02-01 19:20')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2020-02-02 00:34')
stationcalls[trainnumber].append(227)

annotates.append({'datetime':'2020-02-01 18:10','station':0,'text':u'every day\n в Хабаровск'})
'''


# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=2

horizontal_axis_label_format='%H'

x_bounds = [datetime.datetime(2020, 02, 01,00,00), datetime.datetime(2020, 02, 02,8,00)]

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