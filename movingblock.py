import pygame, game, sys, math, random

class Movingblock():	
	def __init__(self, y, speed):
	 
		self.x = 640
		self.y = y
		self.up = False
		self.speedup = random.randint(3,4)/2
		self.ground = y
		self.speed = speed
		self.image =  pygame.image.load('images/movblock.bmp').convert_alpha()
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
	
	def update(self):
		self.x = self.x - self.speed
		
		if self.y > self.ground:
			self.up = True
		elif self.ground - 60 > self.y:
			self.up = False
		
		if self.up == True:
			self.y = self.y - self.speedup
		elif self.up == False:
			self.y = self.y + self.speedup
		
		
	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		game.display.blit(self.image, self.rect)
		