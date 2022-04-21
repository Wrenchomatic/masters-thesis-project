from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import random

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

#Gather data at every X seconds
delay = 10 

yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
colourlist = [yellow, red, blue, green, magenta, cyan]

#Write sensor data to file
with open ('/home/pi/Desktop/sensor_data.csv', "w", newline='') as f:    
    data_writer = writer(f)
    data_writer.writerow(['temp','hum', 'pres', 'datetime'])


while True:
    data = get_sense_data()
    dt = data[-1] - timeStamp
    
    if dt.seconds > delay:
        #f = open('/home/pi/Desktop/sensor_data.csv', "w", newline='')
        with open('/home/pi/Desktop/sensor_data.csv','a') as f: 
            #print("data", data)
            data_writer = writer(f)
            data_writer.writerow(data)
            timeStamp = datetime.now()
            sense.clear(random.choice(colourlist))
        
    
''' DATA LOOKS LIKE THIS
temp,hum,pres,datetime
29.9,22.3,1019.9,2022-01-18 15:35:11.292750
30.0,23.9,1019.9,2022-01-18 15:35:22.294022
30.2,23.3,1019.9,2022-01-18 15:35:33.295579
'''