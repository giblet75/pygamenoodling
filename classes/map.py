import pygame
import random
from pygame.locals import *
from globals import *

class Map:
	def __init__(self, app, width, height):
		self._app = app
		self._width = width
		self._height = height
		self._map = self.generate_map(width, height)

	def on_render(self, display_surf):
		for j in range(self._height / SPRITE_SIZE):
			for i in range(self._width / SPRITE_SIZE):
				#display_surf.blit(self._app.grab_sprite(self._app._sprites["EARTH%d"%((i+j)%6)]), (i*SPRITE_SIZE,j*SPRITE_SIZE))
				display_surf.blit(self._app.grab_sprite(self._map[i][j]), (i*SPRITE_SIZE,j*SPRITE_SIZE))

	def generate_map(self, width, height):
		array = []
		for j in range(height):
			array.append([])
			for i in range(width):
				array[j].append("EARTH%d"%random.randint(0,6))
		return array

