import pygame, game, sys, math, block, random, movingblock, powerup

class Jumpman():
	def __init__(self, y, name, jumpbutton):
	
		self.x = 30
		self.y = y
		self.speed = 3
		self.level = 1
		self.groundlevel = y
		self.jumping = False
		self.character = "ghost"
		self.name = name
		self.image = pygame.image.load('images/'+ self.character+'.bmp').convert_alpha()
		self.jumpbutton = jumpbutton
		self.blocks = []
		self.blockcd = 50
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		self.score = 0
		self.combo = 0
		self.powerups = []
		self.invinsible = False
		self.invinsiblecd = 0 
		self.powerupcd = 230
		self.imagepowerup =  pygame.image.load('images/powerupinvinsible.bmp').convert_alpha()
		
	def update(self):
		self.bewegungsblock = random.randint(0,3)
		pressed_keys = pygame.key.get_pressed()
		
		if pressed_keys[self.jumpbutton]:
			if self.y == self.groundlevel:	
				self.y= self.y - 3
				self.jumping = True
		elif pressed_keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
	
		if self.y != self.groundlevel:
			if self.jumping == True:
				self.y= self.y - 3
				if self.groundlevel-self.y  == 60:
					self.jumping = False
			else:
				self.y = self.y +3
				
		self.blockcd = self.blockcd + 1
		self.powerupcd = self.powerupcd + 1	
		
		if self.blockcd >= 80 - self.level * 5:
			self.blockcd = 0
			if self.bewegungsblock == 0:
				self.movingblockadd()
			elif self.bewegungsblock > 0:
				self.blockadd()
				
		if self.powerupcd == 900:
			self.powerupcd = 0
			self.powerupadd()	
			
				
	def draw(self):	
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		game.display.blit(self.image, self.rect)
		self.blockupdate()
		self.powerupupdate()
		if self.invinsible == True:
			game.display.blit(self.imagepowerup, pygame.Rect(380 ,self.groundlevel - 85 , 20, 20))

		
	def powerupupdate(self):
		for powerup in self.powerups:
			powerup.update()
			powerup.draw()
			if self.rect.colliderect(powerup.rect):
				if powerup.style == 0:
					self.combo = self.combo * 2
				if powerup.style == 1:
					self.invinsible = True
					self.invinsiblecd = 300
		self.powerups = [powerup for powerup in self.powerups if powerup.x > 0 and not self.rect.colliderect(powerup.rect)]
		if self.invinsible == True:
			self.invinsiblecd = self.invinsiblecd -1 
		
		if 	self.invinsiblecd == 0:
			self.invinsible = False
			
	
	def blockupdate(self):
		for block in self.blocks:
			block.update()
			block.draw()
			if block.x < 0:
				self.score = self.score + 1 * self.combo + 1
				self.combo = self.combo + 1
				if self.score > 20 and self.level < 2:
					self.level = self.level + 1
				elif self.score > 50 and self.level < 3:
					self.level = self.level + 1	
				elif self.score > 100 and self.level < 4:
					self.level = self.level + 1	
				elif self.score > 200 and self.level < 5:
					self.level = self.level + 1	
				elif self.score > 300 and self.level < 6:
					self.level = self.level + 1	
				elif self.score > 500 and self.level < 7:
					self.level = self.level + 1	
				elif self.score > 800 and self.level < 8:
					self.level = self.level + 1	
				elif self.score > 1000 and self.level < 9:
					self.level = self.level + 1	

			if self.rect.colliderect(block.rect) and self.invinsible == False:
				self.combo = 0
					
			
		self.blocks = [block for block in self.blocks if block.x > 0 and not self.rect.colliderect(block.rect)]
	
	def blockadd(self):
		self.blocks.append(block.Block(self.groundlevel, self.speed, bool(random.getrandbits(1))))

	def movingblockadd(self):
		self.blocks.append(movingblock.Movingblock(self.groundlevel, self.speed))	
		
	def powerupadd(self):		
		self.powerups.append(powerup.Powerup(self.groundlevel, self.speed, random.randint(0,1)))
		