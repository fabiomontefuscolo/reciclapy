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
from pygame.locals import *

class Keyboard(object):
    def __init__(self):
        self._keys = {}
        self._downs = {}
    def update(self):
        for event in pygame.event.get([KEYDOWN, KEYUP]):
            if event.type == KEYDOWN:
                self._keys[event.key] = True
                self._downs[event.key] = self._downs.get(event.key, 0) + 1
            else:
                self._keys[event.key] = False
    
    def is_pressed(self, key):
        return self._keys.get(key, False)

    def was_pressed(self, key):
        if self._downs.get(key, 0):
            self._downs[key] -= 1
            return True
        return False
            
