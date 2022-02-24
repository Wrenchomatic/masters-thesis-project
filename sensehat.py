from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import random

#TODO
# Optional: Add an average of each sensor value
# Check that it works
# Secure the data?


#Get sensor data from temperature, humidity and pressure sensors
def get_sense_data():
    sense_data = []
    
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    pres = sense.get_pressure()
    
    temp = round(temp,1)
    hum = round(hum,1)
    pres = round(pres,1)
    
    sense_data.append(temp)
    sense_data.append(hum)
    sense_data.append(pres)
    sense_data.append(datetime.now())
    
    return sense_data

sense = SenseHat()
timeStamp = datetime.now()
delay = 3 #Gather data at every X seconds

yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
colourlist = [yellow, red, blue, green, magenta, cyan]

#Write sensor data to file
with open('/home/pi/Desktop/project/masters-thesis-project/djangoWebApp/static/sensor_data.csv','w', newline='') as f:
    
    data_writer = writer(f)
    data_writer.writerow(['temp','hum', 'pres', 'datetime'])
    
    while True:
        data = get_sense_data()
        #print("timeStamp is : ", timeStamp)
        #print("date[-1] is : ", data[-1])
        dt = data[-1] - timeStamp
        
        #Gather data with a delay
        if dt.seconds > delay:
            data_writer.writerow(data)
            timeStamp = datetime.now()
            #sense.show_message("Writing Data", text_colour=yellow)
            sense.clear(random.choice(colourlist))
            
''' DATA LOOKS LIKE THIS
temp,hum,pres,datetime
29.9,22.3,1019.9,2022-01-18 15:35:11.292750
30.0,23.9,1019.9,2022-01-18 15:35:22.294022
30.2,23.3,1019.9,2022-01-18 15:35:33.295579
30.5,21.5,1020.0,2022-01-18 15:35:44.296933
30.7,21.1,1020.0,2022-01-18 15:35:55.297505
30.7,22.5,1020.0,2022-01-18 15:36:06.298269
30.9,23.3,1019.9,2022-01-18 15:36:17.299653
30.9,21.0,1020.0,2022-01-18 15:36:28.300530
31.1,22.3,1020.0,2022-01-18 15:36:39.301647
31.3,22.6,1020.1,2022-01-18 15:36:50.301880
31.4,20.7,1020.1,2022-01-18 15:37:01.302151
31.4,20.0,1020.1,2022-01-18 15:37:12.302732
31.6,22.5,1020.1,2022-01-18 15:37:23.303812
31.8,20.7,1020.0,2022-01-18 15:37:34.304715
31.8,23.0,1020.1,2022-01-18 15:37:45.305422
31.8,20.5,1020.1,2022-01-18 15:37:56.307057
31.9,20.7,1020.0,2022-01-18 15:38:07.308441
32.1,21.9,1020.1,2022-01-18 15:38:18.309144
32.1,19.4,1020.0,2022-01-18 15:38:29.309862
32.1,21.4,1020.0,2022-01-18 15:38:40.311331
32.2,20.9,1020.1,2022-01-18 15:38:51.312179
32.4,19.8,1020.1,2022-01-18 15:39:02.313317
32.5,20.5,1019.7,2022-01-18 15:39:13.313825
32.6,20.9,1020.0,2022-01-18 15:39:24.314658
32.6,20.6,1020.0,2022-01-18 15:39:35.315746
32.6,21.3,1019.9,2022-01-18 15:39:46.316747


'''