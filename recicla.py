#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# TODO: add some documentation to the code

import sys, os, random, time

import pygame 
from pygame.locals import *

from score import Score
from player import PlayerSprite, LEFT, RIGHT
from trash import Metal, Paper, Glass, Plastic
from objects import PlasticObject, MetalObject, GlassObject, PaperObject
from music import Music

from keyboard import Keyboard
from scenario import Scenario

MAXROUNDS = 10

class Game(object):
    def __init__(self, res):
        self.fps = 30
        self.resolution = res
        self.score = Score(MAXROUNDS, "images/scorebg.png", (0,0))
        self.scenarios = [ Scenario("images/scenario1.png", "sounds/env1.ogg"),
                Scenario("images/scenario2.png", "sounds/env2.ogg"),
                Scenario("images/scenario3.png", "sounds/env3.ogg")]
        self.scenario = 0
        self.screen = pygame.display.set_mode(self.resolution, FULLSCREEN)
        self.music = Music()
        self.keyhandler = Keyboard()
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

    def select_player(self):
        img = pygame.image.load("images/select_g.png")
        p=0
        self.screen.blit(img, img.get_rect())
        while True:
            self.keyhandler.update()
            if self.keyhandler.was_pressed(K_ESCAPE):
                sys.exit(0)
            if self.keyhandler.was_pressed(K_RIGHT) or self.keyhandler.was_pressed(262):
                img = pygame.image.load("images/select_b.png")
                p = 1
            if self.keyhandler.was_pressed(K_LEFT) or self.keyhandler.was_pressed(260):
                img = pygame.image.load("images/select_g.png")
                p = 0
            if self.keyhandler.was_pressed(K_SPACE) or self.keyhandler.was_pressed(259):
                return p
            self.screen.blit(img, img.get_rect())
            pygame.display.flip()

    def initialize(self):
        splash = pygame.image.load('images/splash.png')
        self.screen.blit(splash, splash.get_rect())
        pygame.display.flip()
        time.sleep(2)
        
        p = self.select_player()
        if p == 0:
            img = "images/player_g.png"
        else:
            img = "images/player_b.png"
        self.player = PlayerSprite((self.resolution[0]/2, self.resolution[1]-40), img)
        self.gplayer = pygame.sprite.RenderPlain(self.player)
        self.scenarios[self.scenario].start(self.screen)
        self.randomize()
        self.trashes.draw(self.screen)
        self.score.draw(self.screen)


    def randomize(self):
        posicoes = [ 300, 450, 600, 750 ]
        self.trash_list = [
                Metal((posicoes.pop(random.randint(0,3)),300)),
                Paper((posicoes.pop(random.randint(0,2)),300)),
                Plastic((posicoes.pop(random.randint(0,1)),300)),
                Glass((posicoes[0],300)),
        ]
        caps = [ t.cap for t in self.trash_list ]
        trashes = caps + [ t.body for t in self.trash_list ]
        self.caps = pygame.sprite.RenderPlain(*caps)
        self.trashes = pygame.sprite.RenderPlain(*trashes)
 
    def check_keys(self):
            self.keyhandler.update()
            if self.keyhandler.was_pressed(K_ESCAPE):
                sys.exit(0)
            if self.keyhandler.is_pressed(K_LEFT) or self.keyhandler.is_pressed(260):
                self.player.move(LEFT)
            elif self.keyhandler.is_pressed(K_RIGHT) or self.keyhandler.is_pressed(262):
                self.player.move(RIGHT)
            if self.keyhandler.was_pressed(K_SPACE) or self.keyhandler.was_pressed(259):
                self.player.fire()
                self.aux = True

    def check_collision(self):
        objects = [ PlasticObject, GlassObject, PaperObject, MetalObject ]
        if not self.player.object:
            self.player.pick_object(random.choice(objects)())
            self.player.obj.add(self.gplayer)
        self.player.object.clear(self.screen, self.scenarios[self.scenario].background)
        self.player.object.draw(self.screen)
        c = pygame.sprite.spritecollide(self.player.obj, self.trashes, False)
        if c:
            c = c[0]
            self.player.obj.remove(self.gplayer)
            c.add(self.player.object)
            self.player.object.draw(self.screen)
        cap = pygame.sprite.spritecollide(self.player.obj, self.caps, False)
        if cap:
            cap = cap[0]
            # verifica se acertou ou errou!
            if cap.collide(self.player.obj):
                self.music.playApplause()
                self.score.make_round(True)
            else:
                self.music.playHit()
                self.score.make_round(False)
            self.score.draw(self.screen)
            self.player.object.clear(self.screen, self.scenarios[self.scenario].background)
            self.player.obj.kill()
            self.trashes.clear(self.screen, self.scenarios[self.scenario].background)
            self.randomize()
            self.trashes.draw(self.screen)
            self.player.object = False
            
        elif self.player.obj.rect.center[1] < 0:
            self.music.playMistake()
            self.score.make_round(False)
            self.score.draw(self.screen)
            self.player.object.clear(self.screen, self.scenarios[self.scenario].background)
            self.player.obj.kill()
    
    def check_rounds(self):
        if self.score.max_rounds_reached():
            if len(self.scenarios) == self.scenario+1:
                self.do_end()
            self.scenarios[self.scenario].stop()
            self.scenario+=1
            self.scenarios[self.scenario].start(self.screen)
            self.score = Score(MAXROUNDS, "images/scorebg.png", (10,10))
            self.randomize()
            self.trashes.draw(self.screen)
            self.score.draw(self.screen)

    def do_end(self):
        img = pygame.image.load("images/end.png")
        self.screen.blit(img, img.get_rect())
        pygame.display.flip()
        time.sleep(4)
        sys.exit(1)

    def update_player(self):
        self.gplayer.clear(self.screen, self.scenarios[self.scenario].background)
        self.gplayer.update()
        self.player.obj.update()
        self.gplayer.draw(self.screen)

    def mainloop(self):
        while True:
            self.clock.tick(30)
            self.check_keys()
            self.check_collision()
            self.check_rounds()
            self.update_player()
            pygame.display.flip()

def main():
    fullpath = os.path.abspath(sys.argv[0])
    dir = os.path.dirname(fullpath)
    os.chdir(dir)
    pygame.init()
    g = Game((1280, 800))
    g.initialize()
    g.mainloop()

if __name__ == "__main__":
    main()
