import pygame, game, sys

# Game initialization
game.init()

gamestart = 0 #0 vor spiel 1 am laufen 2 fertig

clock = pygame.time.Clock()

#music
pygame.mixer.music.load('music/BitQuest.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.Font(None, 36)
starttext = font.render("Press SPACE to start the game"   , 1, (255, 255, 255))
textpos = starttext.get_rect()
textpos.centerx = game.display.get_rect().centerx
textpos.centery = game.display.get_rect().centery

gamedauer = 0
highscore = 0
highscoreplayer = "timmmmmb"
time = font.render("Zeit:" + str(120 - gamedauer/30),1,(255, 255, 255)) 
# Gameloop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	if gamestart == 0: 
		game.display.fill((0,0,0))
		pressed_keys = pygame.key.get_pressed()
		game.display.blit(starttext, textpos)
		
		if pressed_keys[pygame.K_SPACE]:
			gamestart = 1
			game.display.fill((0,0,0))
			for player in game.players:
				player.score = 0
				player.combo = 0
				player.blocks = []
		elif pressed_keys[pygame.K_ESCAPE]:	
			pygame.quit()
			sys.exit()
		
	if gamestart == 1:
		
		gamedauer = gamedauer + 1
		if gamedauer%30 == 0:
			time = font.render("Zeit:" + str(120 - gamedauer/30),1,(255, 255, 255)) 
		game.update()
		game.draw()
		game.display.blit(time, pygame.Rect(420, 5, 20, 20))
		if gamedauer == 3600:
			gamestart = 2
	
	if gamestart == 2:
		zahl = 0
		zeilenabstand = 30
		game.display.fill((0,0,0))
		pressed_keys = pygame.key.get_pressed()
		game.display.blit(starttext, pygame.Rect(100, 150 + zahl * zeilenabstand, 20, 20))
		zahl = zahl + 1
		for player in game.players:
			if player.score > highscore:
				highscore = player.score
				highscoreplayer = player.name
		
		game.display.blit(font.render("Spieler " + highscoreplayer +" hat gewonnen mit "+ str(highscore), 1, (255, 255, 255)), pygame.Rect(100, 200 + zahl * zeilenabstand, 20, 20))
			
		
		for player in game.players:
			zahl = zahl + 1
			game.display.blit(font.render("Spieler: " + player.name +" Punkte:" +str(player.score), 1, (255, 255, 255)), pygame.Rect(150, 250 + zahl * zeilenabstand, 20, 20))
			
		
		if pressed_keys[pygame.K_SPACE]:
			highscore = 0
			gamestart = 1
			game.display.fill((0,0,0))
			for player in game.players:
				player.score = 0
				player.combo = 0
				player.blockcd = 50
				player.blocks = []
				player.level = 1
				gamedauer = 0
				player.invinsible = False
		elif pressed_keys[pygame.K_ESCAPE]:	
			pygame.quit()
			sys.exit()

	pygame.display.flip()

	clock.tick(30)