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

# Type graph label here

title = u"Железная дорога Софрино - Красноармейск. График движения поездов на конец 2019\n"
title = title+"Sofrino-Krasnoarmeisk. Train diagram for late 2019"

svg_filename = 'Sofrino-Krasnoarmeisk-2019.svg'

# Station names here.
# Keys can be order numbers, or kilometers.

stations=dict()
stations[0]=u"Москва"
stations[44]=u'Софрино'
stations[46]=u'Посёлок Дальний'
stations[49]=u'Рахманово'
stations[53]=u'Фёдоровское'
stations[57]=u'Путилово'
stations[60]=u'Красноармейск'



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

trainnumbers=(6404,6406,6408,6412,6414,6416,6418,6420)
trainnumbers = trainnumbers + (6401,6403,6405,6407,6409,6411,6413,6415,6417,6419)
for id in trainnumbers:
	traintimes[str(id)]=list()
	stationcalls[str(id)]=list()
    
# Type train sheldue for each train
# Date is optional



trainnumber='6404'
traintimes[trainnumber].append('2019-12-29 06:33')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse('2019-12-29 06:33')
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)


trainnumber='6406'
traintimes[trainnumber].append('2019-12-29 08:09')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)

trainnumber='6408'
traintimes[trainnumber].append('2019-12-29 10:24')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)


trainnumber='6412'
traintimes[trainnumber].append('2019-12-29 15:18')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)

trainnumber='6414'
traintimes[trainnumber].append('2019-12-29 16:56')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)


trainnumber='6416'
traintimes[trainnumber].append('2019-12-29 19:37')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)


trainnumber='6418'
traintimes[trainnumber].append('2019-12-29 21:03')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)


trainnumber='6420'
traintimes[trainnumber].append('2019-12-29 23:45')
stationcalls[trainnumber].append(44)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=5)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=9)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=13)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=21)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(60)

#----------------

trainnumber='6401'
traintimes[trainnumber].append('2019-12-29 04:15')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6403'
traintimes[trainnumber].append('2019-12-29 05:38')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6405'
traintimes[trainnumber].append('2019-12-29 07:21')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6407'
traintimes[trainnumber].append('2019-12-29 09:25')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6409'
traintimes[trainnumber].append('2019-12-29 12:00')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6411'
traintimes[trainnumber].append('2019-12-29 14:29')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6413'
traintimes[trainnumber].append('2019-12-29 16:07')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)


trainnumber='6415'
traintimes[trainnumber].append('2019-12-29 18:03')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6417'
traintimes[trainnumber].append('2019-12-29 20:25')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

trainnumber='6419'
traintimes[trainnumber].append('2019-12-29 21:55')
stationcalls[trainnumber].append(60)

frist_call_time=dateutil.parser.parse(traintimes[trainnumber][-1])
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=7)))
stationcalls[trainnumber].append(57)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=14)))
stationcalls[trainnumber].append(53)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=19)))
stationcalls[trainnumber].append(49)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=24)))
stationcalls[trainnumber].append(46)
traintimes[trainnumber].append(str(frist_call_time+datetime.timedelta(minutes=30)))
stationcalls[trainnumber].append(44)

'''
stations[0]=u"Москва"
stations[44]=u'Софрино'
stations[46]=u'Посёлок Дальний'
stations[49]=u'Рахманово'
stations[53]=u'Фёдоровское'
stations[57]=u'Путилово'
stations[60]=u'Красноармейск'
'''
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
plt.savefig(svg_filename)
plt.show()