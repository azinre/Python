from gtts import gTTS
from playsound import playsound
import os


def stringToICAO(name, code):
    decode = []
    for w in name:
        st = ''
        for letter in w:
            st += code[letter] + ' '
        decode.append(st[:len(st) - 1])
    return " ".join(decode)


def main():
    icao_code = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
                 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima', 'm': 'mike',
                 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra',
                 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}

    name = input("Please enter your name: ").lower().split(' ')
    decoded = stringToICAO(name, icao_code)
    myVoice = gTTS(decoded)
    myVoice.save("output.mp3")
    os.system("start output.mp3")


main()
