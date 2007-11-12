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

import pygame

from objects import PlasticObject, MetalObject, GlassObject, PaperObject

class Trash(object):
    def __init__(self, pos):
        self.position = pos
        self.cap = None
        self.body = None

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super(Sprite, self).__init__()
        self.position = pos
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class TrashSprite(Sprite):
    def __init__(self, img, pos):
        super(TrashSprite, self).__init__("images/%s.png" % img, pos)

class TrashCapSprite(Sprite):
    def __init__(self, img, pos):
        super(TrashCapSprite, self).__init__("images/t_%s.png" % img, pos)
    def collide(self, object):
        return isinstance(object, self.acceptable)

class Metal(Trash):
    def __init__(self, pos):
        self.image = "metal"
        self.position = pos
        self.cap = TrashCapSprite(self.image, self.position)
        self.body = TrashSprite(self.image, (self.position[0], self.position[1]+self.cap.image.get_height()*1.5))
        self.cap.acceptable = MetalObject

class Plastic(Trash):
    def __init__(self, pos):
        self.image = "plastic"
        self.position = pos
        self.cap = TrashCapSprite(self.image, self.position)
        self.body = TrashSprite(self.image, (self.position[0], self.position[1]+self.cap.image.get_height()*1.5))
        self.cap.acceptable = PlasticObject

class Glass(Trash):
    def __init__(self, pos):
        self.image = "glass"
        self.position = pos
        self.cap = TrashCapSprite(self.image, self.position)
        self.body = TrashSprite(self.image, (self.position[0], self.position[1]+self.cap.image.get_height()*1.5))
        self.cap.acceptable = GlassObject

class Paper(Trash):
    def __init__(self, pos):
        self.image = "paper"
        self.position = pos
        self.cap = TrashCapSprite(self.image, self.position)
        self.body = TrashSprite(self.image, (self.position[0], self.position[1]+self.cap.image.get_height()*1.5))
        self.cap.acceptable = PaperObject
 
