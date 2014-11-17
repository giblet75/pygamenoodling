#! /usr/bin/env python
import pygame
from pygame.locals import *
from classes.globals import *

from classes.app import App
import json

DATA_DIR="data"
ASSETS_DIR="assets"

def read_map(filename):
	tmp = {}
	mapfile = open("%s/%s.dat"%(DATA_DIR,filename), "r")
	keyfile = open("%s/%s_keys.json"% (DATA_DIR, filename), "r")
	#keys = json.load(keyfile)
	#while line = mapfile.readline

if __name__ == "__main__" :
	file = open(DATA_DIR + "/sprites.json", "r")
	theApp = App()
	theApp._sprites = json.load(file)
	theApp.on_execute("%s/%s"%(ASSETS_DIR, "DungeonCrawl_ProjectUtumnoTileset.png"))
	map = read_map("map")
