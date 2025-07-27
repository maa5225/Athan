import prayerTimes
import ParseTimes
from datetime import datetime

prayerTimes = prayerTimes.get_prayer_times("New York", "USA")
#fajr = 0
#zuhur = 2
#asr = 3
#maghrib = 5
#isha = 6


#print(prayerTimes["Fajr"])

parsedPrayers = ParseTimes.parseTimes(prayerTimes)
#print("parsed prayers: \n", parsedPrayers)

ParseTimes.toTime(parsedPrayers)
