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


import pygame, random

VEL = 25

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super(Object, self).__init__()
        self.shooted = False
        self.position = None

    def shoot(self):
        self.shooted = True

    def update(self):
        if self.shooted:
            self.rect.center = (self.rect.center[0], self.rect.center[1]-VEL)

    def kill(self):
        super(Object, self).kill()
        self.shooted = False

class PlasticObject(Object):
    def __init__(self):
        super(PlasticObject, self).__init__()
        self.image_src = pygame.image.load(random.choice(['images/bottle.png']))
        self.image = self.image_src
        self.rect = self.image.get_rect()

class MetalObject(Object):
    def __init__(self):
        super(MetalObject, self).__init__()
        self.image_src = pygame.image.load(random.choice(['images/tin.png']))
        self.image = self.image_src
        self.rect = self.image.get_rect()

class PaperObject(Object):
    def __init__(self):
        super(PaperObject, self).__init__()
        self.image_src = pygame.image.load(random.choice(['images/news.png']))
        self.image = self.image_src
        self.rect = self.image.get_rect()

class GlassObject(Object):
    def __init__(self):
        super(GlassObject, self).__init__()
        self.image_src = pygame.image.load(random.choice(['images/cup.png']))
        self.image = self.image_src
        self.rect = self.image.get_rect()

