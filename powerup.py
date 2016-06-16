import pygame, game, sys, math

class Powerup():
	def __init__(self, y, speed, style):
	 
		self.x = 640
		
		self.y = y - 40
		self.style = style 	#0 = combo * 2
		
		
		self.speed = speed
		if self.style == 0:
			self.image =  pygame.image.load('images/powerupx2.bmp').convert_alpha()
		elif self.style == 1:
			self.image =  pygame.image.load('images/powerupinvinsible.bmp').convert_alpha()
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
	
	
	def update(self):
		self.x = self.x - self.speed
		
	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		game.display.blit(self.image, self.rect)