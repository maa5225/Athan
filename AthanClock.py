import prayerTimes
from datetime import datetime

prayerTimes = prayerTimes.get_prayer_times("New York", "USA")

timeNow = datetime.now().time()
#print(timeNow)

def next_prayer():
    return None