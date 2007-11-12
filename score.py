import pygame
from pygame.sprite import Sprite
from pygame.font import Font
from pygame.locals import Rect
from pygame.color import Color

class Score(Sprite):
    font = None

    def __init__(self, maxRounds, image, pos):
        super(Score,self).__init__()

        self.points = 0
        self.round = 0

        self.maxRounds = maxRounds
        self.pos = pos
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect().move(*pos)

        self.font = Font( None, 30 )
        self.fgcolor = Color("0xffffff")
        self.bgcolor = Color("0x00000000")

    def draw(self,screen):
        space_width = self.rect.width/4
        screen.blit( self.image, self.rect )

        cx = self.rect.x + 20
        cy = self.rect.y + 20

        # Points
        pic = self.font.render( "%d" % (self.round - self.points),
                    True, 
                    self.fgcolor,  
                    self.bgcolor )  
        screen.blit( pic, (cx,cy) )
            
        # Errors        
        pic = self.font.render( "%d" % self.points, 
                    True,
                    self.fgcolor,
                    self.bgcolor )
        screen.blit( pic, ( cx + space_width, cy ))
        
        # Current Round
        pic = self.font.render( "%d" % self.round,
                    True,
                    self.fgcolor,
                    self.bgcolor )
        screen.blit( pic, ( cx + space_width * 2, cy ))

        
        # Number of rounds
        pic = self.font.render( "%d" % self.maxRounds,
                    True,
                    self.fgcolor,
                    self.bgcolor )
        screen.blit( pic, ( cx + space_width * 3, cy ))

    def make_round(self,didPoint):
        if didPoint:
            self.points += 1
        self.round += 1
        return self.round

    def max_rounds_reached(self):
        return self.round == self.maxRounds

#
#    Debug Area
#
#tela = pygame.display.set_mode((640,480))
#placar = Score( 10, 'placar.png', [0,0] )
#placar.draw(tela)
#pygame.display.flip()


