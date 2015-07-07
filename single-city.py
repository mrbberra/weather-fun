#Creates a scatter plot of the weatherfor the next 5 days.
#Data is pulled from openweathermap.org
#Scatter points are shaded based on cloudiness.

from urllib import urlopen
import sys
from datetime import datetime as dtt
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.cm as cm
import matplotlib.colorbar as cb

def pull_data():
    loctype = raw_input('What type of location descriptor are you using? Please '
                        'enter a number:\n(1) City Name\n(2) Zip Code'
                        '\n(3) City ID\n(4) Latitude/Longitude\n')
    if loctype == '1':
        n = "q=" + raw_input('What is the name of the city? If the city name '
                'is more than one word, please use hyphens instead of spaces, '
                'and leave out periods. (ie. \"St. Petersburg\" would become '
                '\"St-Petersburg\")\n')
        cc = raw_input('Do you have a country code? (y/n)\n')
        if cc == 'y':
            n2 = raw_input('Please type the ISO 3166 Country Code\n')
            n = n + ',' + cc
    elif loctype == '2':
        n = 'zip=' + raw_input('What is the Zip Code?\n')
    elif loctype == '3':
        locstr = 'id='
        n = raw_input('What is the City ID Number?\n')
    elif loctype == '4':
        n = 'lat=' + raw_input('What is the latitude?\n')
        n = n + '&lon=' + raw_input('What is the longitude?\n')
    else:
        sys.exit('Not a valid answer. Ending program.')
    url = 'http://api.openweathermap.org/data/2.5/forecast?' \
            + n + '&units=imperial'
    try:
        res = urlopen(url)
        fct_raw = res.read()
        fct = eval(fct_raw)
    except:
        sys.exit('Error')
    return fct

def high_lows(fct):
    datesDict = {}
    li = fct['list']
    datesli = []
    temp = []
    cloudy = []
    for w in li:
        date = dtt.strptime(w['dt_txt'][:-6],'%Y-%m-%d %H')
        datesli.append(date)
        temp.append((w['main']['temp_max']+w['main']['temp_min'])/2)
        cloudy.append(1-float(w['clouds']['all'])/float(100))
    fulllist = [datesli,temp,cloudy]
    return fulllist

fct = pull_data()
hls = high_lows(fct)
cityname = fct['city']['name']
print cityname
ti = 'Weather forecast for ' + cityname

#plt.scatter(hls[0], hls[1], c=hls[2], s=400)
#plt.gray()
#plt.xlim(xmin=hls[0][0])
#plt.xlim(xmax=hls[0][len(hls[0])-1])
#plt.xticks(rotation=80)
#test.xaxis.sset_major_formatter(dates.DateFormatter('%m/%d %H'))
xmin = hls[0][0]
xmax = hls[0][len(hls[0])-1]
ymin = min(hls[1])-10
ymax = max(hls[1])+10
fig = plt.figure()
fig.suptitle(ti, fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85, bottom=0.3)
ax.set_ylabel('Temperature (Fahrenheit)')
ax.set_xlabel('Time')
ax.scatter(hls[0],hls[1],c=hls[2],cmap=cm.Greys,edgecolor='None',s=400)
ax.axis([xmin,xmax,ymin,ymax])
myFmt = dates.DateFormatter('%m/%d  %H')
ax.xaxis.set_major_formatter(myFmt)
plt.xticks(rotation=45)

plt.show()

