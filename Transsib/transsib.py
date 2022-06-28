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

title = u"Транссибирская железная дорога. График движения поездов на 2022 \n"
title = title+"Transsib railway. Train diagram for 2022. Local time "

svg_filename = 'Transsib railway train diagram 2022.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

#https://transsib.ru/large-st.htm

stations=dict()
stations[5185]="Иркутск"
stations[5311]="Слюдянка"
stations[5477]="Мысовая"
stations[5641]="Улан-Удэ"
stations[6198]="Чита-2"
stations[6587]="Чернышевск"
stations[7306]="Сковородино"
stations[7807]="Свободный"
stations[7866]="Белогорск"
stations[8190]="Облучье"
stations[8351]="Биробиджан"
stations[8523]="Хабаровск"
stations[9177]="Уссурийск"
stations[9289]="Владивосток"

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
'''
trainnumbers=(402,404,406,'604К',408,602,610,'610weekends',412,608)
trainnumbers = trainnumbers + (601,405,403,'603К',407,609,411,401,607,409)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
'''
trainnumbers = list()
# Type train sheldue for each train
# Date is optional
# Local time

#weekdays


trainnumber='002 MOW-VVO'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-07-11 21:23')
stationcalls[trainnumber].append(5185)
traintimes[trainnumber].append('2022-07-11 22:03')
stationcalls[trainnumber].append(5185)
traintimes[trainnumber].append('2022-07-12 06:25')
stationcalls[trainnumber].append(5641) #Улан-Удэ
traintimes[trainnumber].append('2022-07-12 17:43')
stationcalls[trainnumber].append(6198) #Чита
traintimes[trainnumber].append('2022-07-12 18:19')
stationcalls[trainnumber].append(6198) #Чита
traintimes[trainnumber].append('2022-07-14 01:36')
stationcalls[trainnumber].append(7807) #Свободный
traintimes[trainnumber].append('2022-07-14 13:06')
stationcalls[trainnumber].append(8351) #Биробиджан
traintimes[trainnumber].append('2022-07-14 15:35')
stationcalls[trainnumber].append(8523) #Хабаровск
traintimes[trainnumber].append('2022-07-14 16:45')
stationcalls[trainnumber].append(8523) #Хабаровск
traintimes[trainnumber].append('2022-07-15 06:06')
stationcalls[trainnumber].append(9289) #Владивосток


trainnumber='062 MOW-VVO'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-07-12 07:44')
stationcalls[trainnumber].append(5185)
traintimes[trainnumber].append('2022-07-12 08:07')
stationcalls[trainnumber].append(5185)
traintimes[trainnumber].append('2022-07-12 15:09')
stationcalls[trainnumber].append(5641) #Улан-Удэ
traintimes[trainnumber].append('2022-07-13 01:37')
stationcalls[trainnumber].append(6198) #Чита
traintimes[trainnumber].append('2022-07-13 02:13')
stationcalls[trainnumber].append(6198) #Чита
traintimes[trainnumber].append('2022-07-14 07:49')
stationcalls[trainnumber].append(7807) #Свободный
traintimes[trainnumber].append('2022-07-14 18:08')
stationcalls[trainnumber].append(8351) #Биробиджан
traintimes[trainnumber].append('2022-07-14 20:29')
stationcalls[trainnumber].append(8523) #Хабаровск
traintimes[trainnumber].append('2022-07-14 20:59')
stationcalls[trainnumber].append(8523) #Хабаровск
traintimes[trainnumber].append('2022-07-15 09:59')
stationcalls[trainnumber].append(9289) #Владивосток


trainnumber='6830 birobidzan-habarovsk'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-07-14 07:10')
stationcalls[trainnumber].append(8351)
traintimes[trainnumber].append('2022-07-14 09:43')
stationcalls[trainnumber].append(8523)

trainnumber='6862 obluchie-khabarovsk'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-07-14 07:10')
stationcalls[trainnumber].append(8190)
traintimes[trainnumber].append('2022-07-14 10:08')
stationcalls[trainnumber].append(8351)
traintimes[trainnumber].append('2022-07-14 10:16')
stationcalls[trainnumber].append(8351)
traintimes[trainnumber].append('2022-07-14 12:31')
stationcalls[trainnumber].append(8523)

trainnumber='6842 birobidzan-habarovsk'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-07-14 18:25')
stationcalls[trainnumber].append(8351)
traintimes[trainnumber].append('2022-07-14 20:44')
stationcalls[trainnumber].append(8523)




trainnumber='035'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
annotates.append({'datetime':'2022-07-13 21:31','station':7866,'text':u'from Blagoveshensk'})
traintimes[trainnumber].append('2022-07-13 21:31')
stationcalls[trainnumber].append(7866)
traintimes[trainnumber].append('2022-07-13 22:16')
stationcalls[trainnumber].append(7866)
traintimes[trainnumber].append('2022-07-14 05:10')
stationcalls[trainnumber].append(8190)
traintimes[trainnumber].append('2022-07-14 07:52')
stationcalls[trainnumber].append(8351)
traintimes[trainnumber].append('2022-07-14 07:57')
stationcalls[trainnumber].append(8351)
traintimes[trainnumber].append('2022-07-14 10:29')
stationcalls[trainnumber].append(8523)



trainnumber='6366 spassk-vvo'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
annotates.append({'datetime':'2022-07-15 17:56','station':9177,'text':u'Spassk-Dalniy - VVO'})
traintimes[trainnumber].append('2022-07-15 17:56')
stationcalls[trainnumber].append(9177)
traintimes[trainnumber].append('2022-07-15 20:19')
stationcalls[trainnumber].append(9289)



trainnumber='006'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
traintimes[trainnumber].append('2022-07-14 19:40')
stationcalls[trainnumber].append(8523)
traintimes[trainnumber].append('2022-07-15 06:03')
stationcalls[trainnumber].append(9177)
traintimes[trainnumber].append('2022-07-15 07:53')
stationcalls[trainnumber].append(9289)



trainnumber='352'
trainnumbers.append(trainnumber)
traintimes[trainnumber] = list()
stationcalls[trainnumber] = list()
annotates.append({'datetime':'2022-07-14 17:21','station':8523,'text':u'From Sovgavan'})
traintimes[trainnumber].append('2022-07-14 17:21')
stationcalls[trainnumber].append(8523)
traintimes[trainnumber].append('2022-07-14 18:31')
stationcalls[trainnumber].append(8523)
traintimes[trainnumber].append('2022-07-15 07:03')
stationcalls[trainnumber].append(9177)
traintimes[trainnumber].append('2022-07-15 09:08')
stationcalls[trainnumber].append(9289)


# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1
train_color = '#b10026'
horizontal_axis_label_format='%H'

# Time bounds of figure
x_bounds = [datetime.datetime(2022, 7, 11,6,0), datetime.datetime(2022, 7, 15,20,5)]
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
    ax.plot(traintimes[trainnumber],stationcalls[trainnumber],train_line_style,label=trainnumber, color = train_color, antialiased=False)
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
