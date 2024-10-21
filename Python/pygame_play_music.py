from pygame import mixer  # Load the popular external library
import time

def initialize():
    mixer.init()
    mixer.music.load('bday.mp3')

def main():
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

if __name__ == '__main__':
    initialize()
    main()