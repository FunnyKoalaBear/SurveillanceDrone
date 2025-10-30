# CODES
## Connect remotely to raspberry terminal:
```
 «
 ssh drone@(current raspberry ip)
 \\password is hi123
 »

```
## Python program that prints the ENS data every 2 seconds and check different values every 15 seconds

```

import time
import board
import adafruit_ahtx0
import adafruit_ens160

start_time = time.time()

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
aht=adafruit_ahtx0.AHTx0(i2c,address=0x38)
ens = adafruit_ens160.ENS160(i2c,address=0x53)

time_elapsed = 0 
while True:
    AQI = ens.AQI
    TVOC = ens.TVOC
    eCO2 = ens.eCO2
    temp = aht.temperature
    hum = aht.relative_humidity
    #(Air quality index(1-5), Total volatile organic compounds(in ppb), equivalent Carbon Dioxide(in ppm), Temperature (in º), Humidity (in %)) 
    if time_elapsed%2 == 0:
        print(AQI,",",TVOC,",",eCO2,",",temp,",",hum)
        if temp>26:
            print("Too hot")
        if temp<20:
            print("Too cold")
    if time_elapsed ==0:
        hum2 = hum
        hum1 = hum
        eCO21 = eCO2
        eCO22 = eCO2
        TVOC1  = TVOC
        TVOC2 = TVOC
        AQI1 = AQI
        AQI2 = AQI
    if time_elapsed%15 == 0 and time_elapsed !=0:
        hum1 = hum2
        hum2 = hum
        eCO21 = eCO22
        eCO22 = eCO2
        TVOC1 = TVOC2
        TVOC2 = TVOC
        AQI1 = AQI2
        AQI2 = AQI
        print("15 second had passed")
        if abs(hum2-hum1) > 10:
            print("Humidity changed more than 10 in 15 seconds")
        if abs(eCO22-eCO21) >150:
            print("Carbon dioxide level changed more than 150 in 15 seconds")
        if abs(TVOC2-TVOC1) >200:
            print("Total volatile organic compound level changed more than 200 in 15 seconds")
        if abs(AQI2 - AQI1) >1:
            print("Air quality index changed more then 2 in 15 seconds")


    print(time_elapsed)
    time_elapsed += 1
    time.sleep(1)
    
```



