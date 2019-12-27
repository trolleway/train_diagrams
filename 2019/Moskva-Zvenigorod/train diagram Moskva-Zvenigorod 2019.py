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

trainnumbers=(6405,6103,6111,6121,6131,6135,6401,6155,6165,6173,6183,7457,6209,7461,6403,7463,6231)

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

traintimes['6121'].append('2019-12-29 07:28')
stationcalls['6121'].append(0)
traintimes['6121'].append('2019-12-29 08:32')
stationcalls['6121'].append(43)
traintimes['6121'].append('2019-12-29 08:53')
stationcalls['6121'].append(59)

traintimes['6131'].append('2019-12-29 08:28')
stationcalls['6131'].append(0)
traintimes['6131'].append('2019-12-29 09:29')
stationcalls['6131'].append(43)
traintimes['6131'].append('2019-12-29 09:49')
stationcalls['6131'].append(59)

traintimes['6135'].append('2019-12-29 09:18')
stationcalls['6135'].append(0)
traintimes['6135'].append('2019-12-29 10:25')
stationcalls['6135'].append(43)
traintimes['6135'].append('2019-12-29 10:45')
stationcalls['6135'].append(59)

traintimes['6401'].append('2019-12-29 10:30')
stationcalls['6401'].append(0)
traintimes['6401'].append('2019-12-29 11:34')
stationcalls['6401'].append(43)
traintimes['6401'].append('2019-12-29 11:55')
stationcalls['6401'].append(59)

traintimes['6155'].append('2019-12-29 12:03')
stationcalls['6155'].append(0)
traintimes['6155'].append('2019-12-29 13:07')
stationcalls['6155'].append(43)
traintimes['6155'].append('2019-12-29 13:29')
stationcalls['6155'].append(59)

traintimes['6165'].append('2019-12-29 13:48')
stationcalls['6165'].append(0)
traintimes['6165'].append('2019-12-29 14:51')
stationcalls['6165'].append(43)
traintimes['6165'].append('2019-12-29 15:11')
stationcalls['6165'].append(59)

traintimes['6173'].append('2019-12-29 14:58')
stationcalls['6173'].append(0)
traintimes['6173'].append('2019-12-29 15:59')
stationcalls['6173'].append(43)
traintimes['6173'].append('2019-12-29 16:20')
stationcalls['6173'].append(59)

traintimes['6183'].append('2019-12-29 16:18')
stationcalls['6183'].append(0)
traintimes['6183'].append('2019-12-29 17:20')
stationcalls['6183'].append(43)
traintimes['6183'].append('2019-12-29 17:41')
stationcalls['6183'].append(59)

traintimes['7457'].append('2019-12-29 17:57')
stationcalls['7457'].append(0)
traintimes['7457'].append('2019-12-29 18:42')
stationcalls['7457'].append(43)
traintimes['7457'].append('2019-12-29 18:59')
stationcalls['7457'].append(59)

traintimes['6209'].append('2019-12-29 18:48')
stationcalls['6209'].append(0)
traintimes['6209'].append('2019-12-29 19:53')
stationcalls['6209'].append(43)
traintimes['6209'].append('2019-12-29 20:14')
stationcalls['6209'].append(59)





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
x_bounds = [datetime.datetime(2019, 12, 29,10,00), datetime.datetime(2019, 12, 29,20)]

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

print('left,right')
left, right = plt.xlim()
print(left,right)
new_x = matplotlib.dates.datestr2num('2019-12-29 10:25')	
print('newx=',new_x)
	
#ax.set_xlim(left=737422.4340277778)
ax.set_xlim(x_bounds)

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

