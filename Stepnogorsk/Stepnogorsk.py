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

title = u"Степногорская железная дорога. График движения поездов на 2022\n"
title = title+"Stepnogorsk railway. Train diagram for 2022"

svg_filename = 'Stepnogorsk railway.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]="Степногорск"
stations[10]='СПЗ'
stations[20]='ГМЗ'
stations[24]='Заводская'


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

trainnumbers=(404,406,'604К',408,610,412)
trainnumbers = trainnumbers + (405,403,'603К',407,609,411)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()

# Type train sheldue for each train
# Date is optional
# Local time

#weekends

trainnumber='404'
traintimes[trainnumber].append('2022-07-10 07:26')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-10 07:39')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 07:58')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 08:07')
stationcalls[trainnumber].append(24)

trainnumber='406'
traintimes[trainnumber].append('2022-07-10 08:14')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-10 08:35')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 08:55')
stationcalls[trainnumber].append(20)


trainnumber='604К'
traintimes[trainnumber].append('2022-07-10 10:04')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-10 10:22')
stationcalls[trainnumber].append(10)
annotates.append({'datetime':'2022-07-10 10:22','station':10,'text':u'01.04.22 - 15.09.22'})


trainnumber='408'
traintimes[trainnumber].append('2022-07-10 14:55')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-10 15:14')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 15:33')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 15:42')
stationcalls[trainnumber].append(24)


trainnumber='610'
traintimes[trainnumber].append('2022-07-10 18:20')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-10 18:38')
stationcalls[trainnumber].append(10)
annotates.append({'datetime':'2022-07-10 18:38','station':10,'text':u'weekdays 01.04.22 - 15.09.22'})


trainnumber='412'
traintimes[trainnumber].append('2022-07-10 19:40')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2022-07-10 20:01')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 20:22')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 20:31')
stationcalls[trainnumber].append(24)


# down trains


trainnumber='405'
traintimes[trainnumber].append('2022-07-10 09:05')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 09:25')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 09:45')
stationcalls[trainnumber].append(0)

trainnumber='403'
traintimes[trainnumber].append('2022-07-10 09:10')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-10 09:20')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 09:40')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 09:58')
stationcalls[trainnumber].append(0)


trainnumber='603К'
traintimes[trainnumber].append('2022-07-10 10:35')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 10:53')
stationcalls[trainnumber].append(0)


trainnumber='407'
traintimes[trainnumber].append('2022-07-10 16:15')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-10 16:25')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 16:44')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 17:06')
stationcalls[trainnumber].append(0)

trainnumber='609'
traintimes[trainnumber].append('2022-07-10 19:05')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 19:27')
stationcalls[trainnumber].append(0)

trainnumber='411'
traintimes[trainnumber].append('2022-07-10 21:10')
stationcalls[trainnumber].append(24)
traintimes[trainnumber].append('2022-07-10 21:20')
stationcalls[trainnumber].append(20)
traintimes[trainnumber].append('2022-07-10 21:41')
stationcalls[trainnumber].append(10)
traintimes[trainnumber].append('2022-07-10 22:03')
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

vertical_hour_ticks_interval=2

horizontal_axis_label_format='%H'

x_bounds = [datetime.datetime(2022, 7, 10,6,0), datetime.datetime(2022, 7, 10,22,0)]

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
