# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from pygame.mixer import *

class Music:
    alert = 'sounds/alert.ogg'
    beginning = 'sounds/beginning.ogg'
    enviroment1 = 'sounds/enviroment1.ogg'
    enviroment2 = 'sounds/enviroment2.ogg'
    enviroment3 = 'sounds/enviroment3.ogg'
    hit = 'sounds/hit.ogg'
    mistake = 'sounds/mistake.ogg'
    victory = 'sounds/victory.ogg'
    applause = 'sounds/applause.wav'

    def playAlert(self):
        music = pygame.mixer.Sound(self.alert)
        music.play()

    def playBeginning(self):
		music = pygame.mixer.Sound(self.beginning)
		music.play()

    def playEnviroment1(self):
        music = pygame.mixer.Sound(self.enviroment1)
        music.play(-1)

    def playEnviroment2(self):
        music = pygame.mixer.Sound(self.enviroment2)
        music.play(-1)

    def playEnviroment3(self):
        music = pygame.mixer.Sound(self.enviroment3)
        music.play(-1)

    def playFinnish(self):
        music = pygame.mixer.Sound(self.finnish)
        music.play()

    def playHit(self):
        music = pygame.mixer.Sound(self.hit)
        music.play()

    def playApplause(self):
        music = pygame.mixer.Sound(self.applause)
        music.play()

    def playMistake(self):
        music = pygame.mixer.Sound(self.mistake)
        music.play()

    def playVictory(self):
        music = pygame.mixer.Sound(self.victory)
        music.play()

    #def stopAll(self):
    #    pygame.mixer.music.stop()*/

