import requests
import prayerTimes
from datetime import datetime
from datetime import time

def parseTimes(prayer_dict): 
    prayerTimes_list = []
    counter = 0
    for prayerEvent, time in prayer_dict.items():
        prayerTimes_list.append((prayerEvent, time))
        #print("from the actual method call: ", prayerEvent, time)
        #print("Now for the created tuple: ", prayerTimes_list[counter][0], " : ", prayerTimes_list[counter][1], "\n")
        counter+=1
    return prayerTimes_list

def toTime(prayerTimes_list):
    prayer_times = []
    #print("Begin toTime:\n")
    #for num in range(len(prayerTimes_list)):
        #print(prayerTimes_list[num])
    fajr = prayerTimes_list[0][1]
    zuhur = prayerTimes_list[2][1]
    asr = prayerTimes_list[3][1]
    maghrib = prayerTimes_list[5][1]
    isha = prayerTimes_list[6][1]
    prayer_times.append(time(hour=int(fajr[:2]), minute=int(fajr[3:])))
    prayer_times.append(time(hour=int(zuhur[:2]), minute=int(zuhur[3:])))
    prayer_times.append(time(hour=int(asr[:2]), minute=int(asr[3:])))
    prayer_times.append(time(hour=int(maghrib[:2]), minute=int(maghrib[3:])))
    prayer_times.append(time(hour=int(isha[:2]), minute=int(isha[3:])))
    print(prayer_times)