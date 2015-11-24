import time
import pygame
pygame.init()
pygame.mixer.init()
bowl = pygame.mixer.Sound("singing-bowl-strike-sound.wav")
ring = pygame.mixer.Sound("ring-sound.wav")

def ringgg():
    ring.play()
    print("ringgg!")
    time.sleep(10)


def ding():
    bowl.play()
    print("Ding!")
    time.sleep(10)

while True:
    ding()
    ringgg()

#to add:
#user input for how far apart the sounds are.
#user input to change tehe tones
#user input for how long to run program.



#ring-sound.wav
