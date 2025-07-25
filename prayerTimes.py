from datetime import datetime
import requests

#print(datetime.today().strftime("%m-%d-%y"))

def get_prayer_times(city, country, method=2):
    url = "https://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city,
        "country" : country,
        "method": method,
        "date": datetime.today().strftime("%m-%d-%y")
    }

    response = requests.get(url, params= params)

    if response.status_code == 200:
        data = response.json()["data"]["timings"]
        #print(f"Prayer Times for {city}, {country}:")
        #for prayer, time in data.items(): 
            #print(f"{prayer}: {time}")
        return data
    else:
        print("Error fetching prayer times:", response.status_code, response.text)
        return None
    
#data = get_prayer_times("New York", "USA")