import pygame, game, sys, math

class Block():
	def __init__(self, y, speed, oben):
	 
		self.x = 640
		if oben == True:
			self.y = y - 40
		else:
			self.y = y
		
		
		self.speed = speed
		self.image =  pygame.image.load('images/block.bmp').convert_alpha()
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
	
	def update(self):
		self.x = self.x - self.speed
		
	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		game.display.blit(self.image, self.rect)
		