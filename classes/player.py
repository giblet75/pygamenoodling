import pygame
from pygame.locals import *
from globals import *

class Player:
	def __init__(self):
		self._x = 0
		self._y = 0
		self._sprite = None
		self._robe = None

	def on_render(self, display_surf):
		display_surf.blit(self._sprite, (self._x*SPRITE_SIZE,self._y*SPRITE_SIZE), None, BLEND_RGBA_MAX)
		display_surf.blit(self._robe, (self._x*SPRITE_SIZE,self._y*SPRITE_SIZE), None, BLEND_RGBA_ADD)
