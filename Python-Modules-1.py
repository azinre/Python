import random
from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 105, 180)
gray = (220, 220, 220)


def rollAdice(num_dice):
    outcome = random.randint(1, num_dice)
    print(outcome)
    return outcome


def diceLogo(num_dice):
    w = white
    b = black
    frame = [
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
    ]
    for i in range(num_dice):
        frame[i] = b
    return(frame)


def main():
    user_input_right_value = False
    while not user_input_right_value:
        try:
            num_dice = int(input('How many faces should the dice have [1-64]?'))
            if 1 <= num_dice < 65:
                user_input_right_value = True
            else:
                print("Enter a valid number between 1-64")
        except:
            print("Enter a valid number between 1-64")
    outcome = rollAdice(num_dice)
    s.set_pixels(diceLogo(outcome))


while True:
    main()
