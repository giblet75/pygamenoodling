#! /usr/bin/env python
import pygame
from pygame.locals import *
from globals import *

from player import Player
from map import Map

ASSETS_DIR="../assets"

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self._size = self._width, self._height = 1024, 768
		self._sprite_sheet = None
		self._sprites = None
		self._x = 1
		self._y = 2
		self._player = None

	def on_init(self, spritesheet_filename):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._sprite_sheet = pygame.image.load(spritesheet_filename).convert()
		self._sprite_sheet = pygame.transform.scale(self._sprite_sheet, (2048*2, 1536 * 2))
		self._running = True
		self._player = Player()
		self._map = Map(self, self._width, self._height)
		self._player._sprite = self.grab_sprite("PLAYER_MALE")
		self._player._robe = self.grab_sprite("ROBE0")
		self._player._x = 1
		self._player._y = 2

	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				self._running = False
			if event.key == K_h:
				self._player._x -= 1
			if event.key == K_l:
				self._player._x += 1
			if event.key == K_j:
				self._player._y += 1
			if event.key == K_k:
				self._player._y -= 1
	
	def on_loop(self):
		pass

	def on_render(self):
		for i in range(0):
			self._display_surf.blit(self.grab_sprite(self._sprites["EARTH%d"%i]), (i*SPRITE_SIZE,0))
			self._display_surf.blit(self.grab_sprite(self._sprites["EARTH%d"%((i+1)%6)]), (i*SPRITE_SIZE,SPRITE_SIZE))
			self._display_surf.blit(self.grab_sprite(self._sprites["EARTH%d"%((i+2)%6)]), (i*SPRITE_SIZE,2*SPRITE_SIZE))
			self._display_surf.blit(self.grab_sprite(self._sprites["EARTH%d"%((i+3)%6)]), (i*SPRITE_SIZE,3*SPRITE_SIZE))
			self._display_surf.blit(self.grab_sprite(self._sprites["EARTH%d"%((i+4)%6)]), (i*SPRITE_SIZE,4*SPRITE_SIZE))
			self._display_surf.blit(self.grab_sprite(self._sprites["EARTH%d"%((i+5)%6)]), (i*SPRITE_SIZE,5*SPRITE_SIZE))
		self._map.on_render(self._display_surf)
		self._player.on_render(self._display_surf)
		pygame.display.flip()

	def on_cleanup(self):
		pygame.quit()
		print "Bye!"

	def on_execute(self, sprite_filename):
		if self.on_init(sprite_filename) == False:
			self._running = False

		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

	def grab_sprite(self, sprite_name):
		coord = self._sprites[sprite_name]
		rect = pygame.Rect((0,0,SPRITE_SIZE,SPRITE_SIZE))
		image = pygame.Surface(rect.size).convert()
		image.blit(self._sprite_sheet, rect, (coord[0]*SPRITE_SIZE, coord[1]*SPRITE_SIZE, (coord[0]+1)*SPRITE_SIZE, (coord[1]+1)*SPRITE_SIZE))
		return image
