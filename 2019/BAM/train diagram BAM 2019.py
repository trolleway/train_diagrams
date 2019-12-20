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


traintimes['097']=list()
stationcalls['097']=list()
traintimes['087']=list()
stationcalls['087']=list()
traintimes['376']=list()
stationcalls['376']=list()
traintimes['348']=list()
stationcalls['348']=list()
traintimes['092']=list()
stationcalls['092']=list()

traintimes['364']=list()
stationcalls['364']=list()
traintimes['364-2']=list()
stationcalls['364-2']=list()

traintimes['097'].append('2018-06-01 20:51')
stationcalls['097'].append(0)

traintimes['376'].append('2018-06-01 11:04')
stationcalls['376'].append(0)

traintimes['348'].append('2018-06-01 03:40')
stationcalls['348'].append(0)

traintimes['092'].append('2018-06-01 12:56')
stationcalls['092'].append(0)






#traintimes['097'].append('2018-06-02 09:17')
#stationcalls['097'].append(717)

traintimes['097'].append('2018-06-02 15:34')
stationcalls['097'].append(1057)

traintimes['376'].append('2018-06-02 07:18')
stationcalls['376'].append(1057)

traintimes['348'].append('2018-06-02 04:48')
stationcalls['348'].append(1057)

traintimes['092'].append('2018-06-02 08:50')
stationcalls['092'].append(1057)


traintimes['097'].append('2018-06-03 18:13')
stationcalls['097'].append(2340)

traintimes['376'].append('2018-06-03 10:30')
stationcalls['376'].append(2340)





traintimes['364'].append('2018-06-03 10:55')
stationcalls['364'].append(2340)
traintimes['364-2'].append('2018-06-04 10:55')
stationcalls['364-2'].append(2340)

traintimes['364'].append('2018-06-05 00:05')
stationcalls['364'].append(3800)
traintimes['364-2'].append('2018-06-06 00:05')
stationcalls['364-2'].append(3800)

stations=dict()
stations[0]=u"Тайшет"
#stations[717]=u'Лена'
stations[1057]=u'Северобайкальск'
stations[2340]=u'Тында'
#stations[3290]=u'Новый Ургал'
stations[3800]=u'Комсомольск-на-Амуре'
stations[4310]=u'Советская Гавань'

title=u"БАМ. График движения поездов на конец 2019\n"
title = title+"BAM. Train diagram for late 2019"

#TIMEZONE is MSK+6
time_add = datetime.timedelta(hours=6)

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
hours = mdates.HourLocator(interval=6) 
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
plt.savefig("train diagram BAM 2019.svg")
plt.show()

