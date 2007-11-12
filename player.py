#!/usr/bin/python
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

MUNIT = 15

LEFT = -MUNIT
RIGHT = MUNIT

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        super(PlayerSprite, self).__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.position = pos
        self.object = None
        self.hold_object = False
    def move(self, side):
        self.position = (self.position[0]+side, self.position[1])
        if self.hold_object:
            self.obj.rect.center = (self.position[0]+25, self.position[1]-5)
    def update(self):
        self.rect.center = self.position
    def fire(self):
        self.hold_object = False
        self.obj.shoot()
    def pick_object(self, obj):
        self.hold_object = True
        self.obj = obj
        self.obj.rect.center = (self.position[0]+25, self.position[1]-5)
        self.object = pygame.sprite.RenderPlain(obj)
