import ConfigParser
import Adafruit_BBIO.GPIO as GPIO
import requests
import time

#TEMPORARY CODE FOR TESTING
GREEN_LED = "P8_7"
RED_LED = "P8_8"
GPIO.setup("P8_7", GPIO.OUT)
GPIO.setup("P8_8", GPIO.OUT)
#END TEMP CODE


Config = ConfigParser.ConfigParser()
Config.read('../config.ini')

clientid = Config.get('API', 'clientid')
#channelname = Config.get('API', 'channelname')
#TODO Correct this
channelname = "amperture"

url = "https://api.twitch.tv/kraken/"
headers = {
        'Client-ID': clientid
        }

apicall = url + "channels/" + channelname + "/" + "follows"

while True: 
    #TODO: LOOK INTO InsecurePlatformWarning
    r = requests.get(apicall, headers=headers)

    with open('latestfollower', "r") as f:
        stored = f.read()

    latest = r.json()["follows"][0]['user']['display_name']
    if latest != stored:
            with open('latestfollower', "w+") as f:
                    f.write(latest)

            GPIO.output(GREEN_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(RED_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(GREEN_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(RED_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(GREEN_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(RED_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(GREEN_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(0.1)

            GPIO.output(RED_LED, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(GREEN_LED, GPIO.LOW)
