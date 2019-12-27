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

trainnumbers=(6405,6103,6111)

for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()

traintimes['6103'].append('2019-12-29 04:41')
stationcalls['6103'].append(0)
traintimes['6103'].append('2019-12-29 05:51')
stationcalls['6103'].append(43)
traintimes['6103'].append('2019-12-29 06:12')
stationcalls['6103'].append(59)

traintimes['6111'].append('2019-12-29 06:03')
stationcalls['6111'].append(0)
traintimes['6111'].append('2019-12-29 07:05')
stationcalls['6111'].append(43)
traintimes['6111'].append('2019-12-29 07:25')
stationcalls['6111'].append(59)





stations=dict()
stations[0]=u"Москва-Смоленская"
#stations[717]=u'Лена'
stations[43]=u'Голицыно'
stations[59]=u'Звенигород'


title=u"Звенигородская ветка. График движения поездов на конец 2019\n"
title = title+"Zvenigorod branch. Train diagram for late 2019"

#TIMEZONE is MSK
time_add = datetime.timedelta(hours=0)

# end of data

def convert_dates(times_list):
    n = list()
    for i in times_list:
        #temp_dt = matplotlib.dates.datestr2num(i)
        temp_dt = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M') + time_add
        n.append(temp_dt)
        print(i)
        print(temp_dt)

    return(n)

for k in traintimes:
    temp_dict=dict()
    temp_dict=convert_dates(traintimes[k])
    traintimes[k] = temp_dict
   
fig, ax = plt.subplots(figsize=(9,9))


# styling
train_line_style='g-'
hours = mdates.HourLocator(interval=1) 
hours_fmt = mdates.DateFormatter('%d %H:%M')  
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
plt.savefig("train diagram Moscow-Zvenigorod 2019.svg")
plt.show()

