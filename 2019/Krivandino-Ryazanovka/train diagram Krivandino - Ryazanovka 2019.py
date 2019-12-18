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
from transliterate import translit, get_available_language_codes

# data sample
traintimes=dict()
stationcalls=dict()

traintimes['6684'] = ['09:17','10:39','11:05','11:13']
stationcalls['6684'] = [0, 40, 53, 53]
traintimes['6690'] = ['15:00','16:22','16:48','16:56']
stationcalls['6690'] = [0, 40, 53, 53]
traintimes['6694'] = ['21:05','22:27','22:53','23:59']
stationcalls['6694'] = [0, 40, 53, 53]

traintimes['6683'] = ['06:10','06:48','07:58','09:17']
stationcalls['6683'] = [53, 40, 0, 0]
traintimes['6687'] = ['11:13','11:40','13:00','15:00']
stationcalls['6687'] = [53, 40, 0, 0]
traintimes['6691'] = ['16:56','17:23','18:42','21:05']
stationcalls['6691'] = [53, 40, 0,0]

stations=dict()
stations[0]=u"Кривандино"
stations[40]=u'Сазоново'
stations[53]=u'Рязановка'

title=u"Кривандино - Рязановка. График движения поездов на конец 2019\n"
title = title+"Krivandino - Ryazanovka. Train diagram for late 2019"

# end of data

def convert_dates(times_list):
    n = list()
    for i in times_list:
        #temp_dt = matplotlib.dates.datestr2num(i)
        temp_dt = datetime.datetime.strptime(i, '%H:%M')
        n.append(temp_dt)
        print(i)
        print(temp_dt)

    return(n)

for k in traintimes:
    temp_dict=dict()
    temp_dict=convert_dates(traintimes[k])
    traintimes[k] = temp_dict
   
fig, ax = plt.subplots(figsize=(9,4))


# styling
train_line_style='g-'
hours = mdates.HourLocator() 
hours_fmt = mdates.DateFormatter('%H:%M')  
plt.title(title)

#transliterate station names
#may be replaced to load dataset with official latin names
for id in stations:
    stations[id] = stations[id]+"\n"+translit(stations[id], 'ru',reversed=True)



# end styling

# station labels generate
station_names=list()
station_pks=list()
for elem in sorted(stations.items()) :
    print(elem[0] , " ::" , elem[1] )
    station_names.append(elem[1])
    station_pks.append(elem[0])
    

plt.yticks(station_pks)
ax.set_yticklabels(station_names)

for trainnumber in traintimes:
    print(trainnumber)
    ax.plot(traintimes[trainnumber],stationcalls[trainnumber],train_line_style,label=trainnumber, color = 'gray', antialiased=False)
    #ax.set_ylabel(r'stations')
    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(hours_fmt)

    plt.gcf().autofmt_xdate()
    ax.grid(True)



    
#plt.legend(title='Trains:')
plt.savefig("train diagram Krivandino - Ryazanovka 2019.svg")
plt.show()

