import random
from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
lightGreen = (75, 245, 56)
blue = (0, 0, 255)
darkBlue = (45, 43, 74)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


def LedsOnForHumidity(room_humidity):
    humidity_percentage = int((room_humidity / 100) * 64)
    s.set_pixels(([blue] * humidity_percentage) + ([white] * (64 - humidity_percentage)))


def displayColorForTemperature(room_temprature):
    if -40 <= room_temprature <= -10:
        s.set_pixels([darkBlue] * 64)
    elif -9 <= room_temprature <= 0:
        s.set_pixels([blue] * 64)
    elif 1 <= room_temprature <= 15:
        s.set_pixels([lightGreen] * 64)
    elif 16 <= room_temprature <= 21:
        s.set_pixels([green] * 64)
    elif room_temprature == 22:
        s.set_pixels([red] * 64)


def main():
    user_input_right_value = False
    while not user_input_right_value:
        try:
            room_temperature = float(input('What is the room temperature?'))
            if -40.0 <= room_temperature < 23.0:
                displayColorForTemperature(room_temperature)
                user_input_right_value = True
            else:
                print("Enter a valid number between -40,23")
        except:
            print("Enter a valid number between -40,22")
    user_input_right_value = False
    while not user_input_right_value:
        try:
            room_humidity = int(input('What is the room humidity?'))
            LedsOnForHumidity(room_humidity)
            user_input_right_value = True
        except:
            print("Enter a valid number between -40,22")


while True:
    main()