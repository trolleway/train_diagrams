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

title = u"Токио - Осака с остановками по линиям 1067мм\n"
title = title+"Tokyo - Osaka for railfaning via 1067mm lines "

svg_filename = 'Tokyo - Osaka local trains.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]="Tokyo"
stations[104]="Atami"
stations[141]="Yoshiwara"
stations[149]="Fujikawa"
stations[257]='Hamamatsu'
stations[293]='Toyohashi'
stations[366]='JR Nagoya'
stations[410]='Ōgaki'
stations[445]='Maibara'
stations[513]='Kyoto'
stations[513+42]='Osaka'


# You can get kilometers from OpenStreetMap under open license at
#http://brouter.de/brouter-web/#map=10/55.5838/37.2927/standard,HikeBike.HillShading&lonlats=37.581269,55.777273;36.881192,55.700614&profile=rail

# kilometers for Japan
# https://en.wikipedia.org/wiki/T%C5%8Dkaid%C5%8D_Main_Line

#transliterate station names
#may be replaced to load dataset with official latin names
from transliterate import translit, get_available_language_codes
for id in stations:
    if ' км' in stations[id]: continue
    if translit(stations[id], 'ru',reversed=True) != stations[id]:
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

trainnumbers=(10,12,14,16,18,20)
trainnumbers = trainnumbers + (601,405,403,'603К',407,609,411,401,607,409)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()

# Type train sheldue for each train
# Date is optional
# Local time

#weekdays


trainnumber='10'
traintimes[trainnumber].append('2024-06-07 10:02')
stationcalls[trainnumber].append(0)
traintimes[trainnumber].append('2024-06-07 11:57')
stationcalls[trainnumber].append(104)


trainnumber='12'
traintimes[trainnumber].append('2024-06-07 12:08')
stationcalls[trainnumber].append(104)
traintimes[trainnumber].append('2024-06-07 12:51')
stationcalls[trainnumber].append(141)
traintimes[trainnumber].append('2024-06-07 12:59')
stationcalls[trainnumber].append(149)
traintimes[trainnumber].append('2024-06-07 14:43')
stationcalls[trainnumber].append(257)

trainnumber='14'
traintimes[trainnumber].append('2024-06-07 14:47')
stationcalls[trainnumber].append(257)
traintimes[trainnumber].append('2024-06-07 15:21')
stationcalls[trainnumber].append(293)

trainnumber='16'
traintimes[trainnumber].append('2024-06-07 15:32')
stationcalls[trainnumber].append(293)
traintimes[trainnumber].append('2024-06-07 17:02')
stationcalls[trainnumber].append(410)

trainnumber='18'
traintimes[trainnumber].append('2024-06-07 17:09')
stationcalls[trainnumber].append(410)
traintimes[trainnumber].append('2024-06-07 17:44')
stationcalls[trainnumber].append(445)

trainnumber='20'
traintimes[trainnumber].append('2024-06-07 17:47')
stationcalls[trainnumber].append(445)
traintimes[trainnumber].append('2024-06-07 18:44')
stationcalls[trainnumber].append(513)
traintimes[trainnumber].append('2024-06-07 19:13')
stationcalls[trainnumber].append(555)




annotates.append({'datetime':'2024-06-07 10:02','station':104,'text':u'JR East / JR Central Terminus of local trains'})
annotates.append({'datetime':'2024-06-07 10:02','station':141,'text':u'Gakunan line: branch with small EMU. 3 hour to visit'})
annotates.append({'datetime':'2024-06-07 13:02','station':149,'text':u'Viewpoint to trains with Fuji mount from platform to Tokyo. 40 min to visit'})
annotates.append({'datetime':'2024-06-07 10:02','station':257,'text':u'Terminus of local trains. Local light railway northbound.'})
annotates.append({'datetime':'2024-06-07 10:02','station':293,'text':u'City tram line. 3 hour to visit'})
annotates.append({'datetime':'2024-06-07 10:02','station':410,'text':u'Terminus of local trains'})
annotates.append({'datetime':'2024-06-07 10:02','station':445,'text':u'JR Central / JR West Terminus of local trains'})

annotates.append({'datetime':'2024-06-07 12:12','station':104,'text':u'Local train wave'})



# down trains





# end of data

# STYLING

# Line style, see refrence at https://matplotlib.org/2.0.2/api/lines_api.html
train_line_style='g-'

vertical_hour_ticks_interval=1
train_color = '#b10026'
horizontal_axis_label_format='%H'

# Time bounds of figure
x_bounds = [datetime.datetime(2024, 6, 7,10,0), datetime.datetime(2024, 6, 7,21,5)]
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
plt.savefig(svg_filename.replace('.svg','.png'))
plt.show()
