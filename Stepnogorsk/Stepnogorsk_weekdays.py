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

title = u"Степногорская железная дорога. График движения поездов на 2022 рабочие\n"
title = title+"Stepnogorsk railway. Train diagram for 2022 weekdays"

svg_filename = 'Stepnogorsk railway train diagram 2022 weekdays.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]="Степногорск"
stations[3]="3 км"
stations[5]="Дачи"
stations[8]="Пляж"
stations[10]='СПЗ'
stations[16]='16 км'
stations[18]='Промышленная'
stations[19]='Химзавод'
stations[20]='ГМЗ'
stations[23]='Электродепо'
stations[24]='Заводская'


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

trainnumbers=(402,404,406,'604К',408,602,610,'610weekends',412,608)
trainnumbers = trainnumbers + (601,405,403,'603К',407,609,411,401,607,409)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()

# Type train sheldue for each train
# Date is optional
# Local time

#weekdays


trainnumber='402'
traintimes[trainnumber].append('2022-07-11 06:35')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 06:53')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 06:54')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 07:05')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 07:13')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 07:22')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 07:32')
stationcalls[trainnumber].append(24)

trainnumber='602'
traintimes[trainnumber].append('2022-07-11 06:45')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 06:57')
stationcalls[trainnumber].append(10)


trainnumber='404'
traintimes[trainnumber].append('2022-07-11 07:26')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 07:39')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 07:49')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 07:50')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 07:58')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 08:07')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 09:10')
stationcalls[trainnumber].append(24)

trainnumber='406'
traintimes[trainnumber].append('2022-07-11 08:14')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 08:35')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 08:48')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 08:55')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 09:05')
stationcalls[trainnumber].append(20)

'''
trainnumber='604К'
traintimes[trainnumber].append('2022-07-11 10:04')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 10:22')
stationcalls[trainnumber].append(10)
annotates.append({'datetime':'2022-07-11 10:22','station':10,'text':u' weekends 01.04.22 - 15.09.22'})
'''

trainnumber='408'
traintimes[trainnumber].append('2022-07-11 14:55')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 15:14')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 15:25')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 15:33')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 15:42')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 16:15')
stationcalls[trainnumber].append(24)


trainnumber='610'
traintimes[trainnumber].append('2022-07-11 16:00')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 16:13')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 16:23')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 16:33')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 16:41')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 16:50')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 17:15')
stationcalls[trainnumber].append(24)


trainnumber='608'
traintimes[trainnumber].append('2022-07-11 16:04')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 16:22')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 16:32')
stationcalls[trainnumber].append(10)


'''
trainnumber='610weekends'
traintimes[trainnumber].append('2022-07-11 18:20')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 18:38')
stationcalls[trainnumber].append(10)
annotates.append({'datetime':'2022-07-11 18:38','station':10,'text':u'weekends 01.04.22 - 15.09.22'})
'''

trainnumber='412'
traintimes[trainnumber].append('2022-07-11 19:40')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-11 20:01')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 20:14')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 20:22')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 20:31')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 21:10')
stationcalls[trainnumber].append(24)


# down trains

trainnumber='601'
traintimes[trainnumber].append('2022-07-11 06:57')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 07:07')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 07:25')
stationcalls[trainnumber].append(0)


trainnumber='401'
traintimes[trainnumber].append('2022-07-11 07:32')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 07:42')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 07:49')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 07:50')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 08:01')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 08:13')
stationcalls[trainnumber].append(0)


trainnumber='405'
traintimes[trainnumber].append('2022-07-11 09:05')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 09:12')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 09:13')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 09:25')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 09:45')
stationcalls[trainnumber].append(0)

trainnumber='403'
traintimes[trainnumber].append('2022-07-11 09:10')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 09:20')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 09:27')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 09:28')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 09:40')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 09:58')
stationcalls[trainnumber].append(0)


trainnumber='607'
traintimes[trainnumber].append('2022-07-11 16:22')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 16:32')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 16:50')
stationcalls[trainnumber].append(0)


trainnumber='407'
traintimes[trainnumber].append('2022-07-11 16:15')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 16:25')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 16:32')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 16:33')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 16:44')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 17:06')
stationcalls[trainnumber].append(0)


trainnumber='409'
traintimes[trainnumber].append('2022-07-11 17:15')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 17:25')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 17:32')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 17:34')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 17:45')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 18:03')
stationcalls[trainnumber].append(0)


trainnumber='411'
traintimes[trainnumber].append('2022-07-11 21:10')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-11 21:20')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-11 21:27')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 21:28')
stationcalls[trainnumber].append(18)
traintimes[trainnumber].append('2022-07-11 21:41')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-11 22:03')
stationcalls[trainnumber].append(0)



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

vertical_hour_ticks_interval=1
train_color = '#b10026'
horizontal_axis_label_format='%H'

# Time bounds of figure
x_bounds = [datetime.datetime(2022, 7, 11,6,0), datetime.datetime(2022, 7, 11,22,5)]
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
    print(trainnumber)
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
