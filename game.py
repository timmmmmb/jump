import jumpman, block, pygame

def init():
	pygame.init()
	global display
	display = pygame.display.set_mode((640, 480))
	
	global font
	font = pygame.font.Font(None, 36)
	
	global players
	players = []
	player1 = jumpman.Jumpman(90,"Player1", pygame.K_SPACE)
	player2 = jumpman.Jumpman(210,"Player2", pygame.K_RETURN)
	player3 = jumpman.Jumpman(330,"Player3", pygame.K_UP)
	player4 = jumpman.Jumpman(450,"Player4", pygame.K_KP_PLUS )
	players.append(player1)
	players.append(player2)
	players.append(player3)
	players.append(player4)
	pygame.display.set_caption('Jump by Tim Frey')

def draw():
	global display
	display.fill((0,0,0))
	for player in players:
		player.draw()
		pygame.draw.rect(display,(255,255,255),pygame.Rect(0, player.groundlevel + 20, 640, 5),5)
		display.blit(font.render("Score: " + str(player.score), 1, (255, 255, 255)), pygame.Rect(50, player.groundlevel - 85, 20, 20))
		display.blit(font.render("Combo: " + str(player.combo), 1, (255, 255, 255)), pygame.Rect(250, player.groundlevel - 85, 20, 20))
		
def update():
	for player in players:
		player.update()