import pygame

class Scenario(object):
        def __init__( self, background, sound ):
                self.background = pygame.image.load(background)
                self.rect = self.background.get_rect()
                self.sound = pygame.mixer.Sound(sound)

        def start( self, screen ):
                screen.blit( self.background, self.rect )
                pygame.display.flip()
                self.sound.play(-1)

        def stop(self):
                self.sound.stop()

