import sys
import urllib2
from gpiozero import CPUTemperature
from time import sleep, strftime, time
#import matplotlib.pyplot as plt

#plt.ion()
#x = []
#y = []
myAPI = 'M7VEPYCYZDWU534O'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
cpu = CPUTemperature()
with open("cpu_temp.csv","a") as log:
    while True:

        temp = cpu.temperature
        """y.append(temp)
        x.append(time())
        plt.clf()
        plt.scatter(x,y)
        plt.plot(x,y)
        plt.draw()"""
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))) #to log the data in csv file
        sleep(1)
        conn = urllib2.urlopen(baseURL + '&field1=%s' % temp) #connection with thingspeak channel
        print conn.read()
        conn.close()
        

