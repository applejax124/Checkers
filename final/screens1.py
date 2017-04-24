#!~pbui/pub/anaconda2-4.1.1/bin

import pygame

pygame.init()
swidth = 800
sheight = 800

screen = pygame.display.set_mode((swidth, sheight))
clock = pygame.time.Clock()
done = False

def homeScreen(screen):
	pygame.font.init()
	#background = pygame.Surface((swidth, sheight))
	#font = "comicsansms"
	font = "forque"
	font1 = pygame.font.SysFont(font, 230)
	checkersText = font1.render("Checkers", True, (250, 220, 5))
	font2 = pygame.font.SysFont(font, 60)
	player1Text = font2.render("One Player", True, (250, 220, 5))
	player2Text = font2.render("Two Players", True, (250, 220, 5))
	font3 = pygame.font.SysFont(font, 50)
	groupText1 = font3.render("Group Members: Cami Carballo", True, (66, 8, 165))
	groupText2 = font3.render("Kendyll, Kraus, Allison Raines, Anna Smith", True, (66, 8, 165))
	background = pygame.image.load('board.png')
	pygame.transform.scale(background, (swidth, sheight), screen)
	#screen.draw.text("Checkers", (25, 50), owidth=1, ocolor=(0, 0, 0))
	screen.blit(checkersText, (30, 100))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 425, 300, 120))
	screen.blit(player1Text, (85, 465))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(450, 425, 300, 120))
	screen.blit(player2Text, (475, 465))
	screen.blit(groupText1, (130, 700))
	screen.blit(groupText2, (40, 750))
	
#pass in results and this will display them based off of that
def resultScreen(winner, screen):
	pygame.font.init()
	font = "forque"
	font1 = pygame.font.SysFont(font, 185)
	font2 = pygame.font.SysFont(font, 100)
	playAgainText = font2.render("Play Again", True, (250, 220, 5))
	background = pygame.image.load('board.png')
	pygame.transform.scale(background, (swidth, sheight), screen)
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 450, 500, 200))
	screen.blit(playAgainText, (225, 510))

	#choose which one based on passed in parameters
	if winner == 1:
		p1Text = font1.render("Player One", True, (250, 220, 5))
		winsText = font1.render("Wins!", True, (250, 220, 5))
		screen.blit(p1Text, (55, 50))
		screen.blit(winsText, (225, 200))
	elif winner == 2:
		p2Text = font1.render("Player Two", True, (250, 220, 5))
		winsText = font1.render("Wins!", True, (250, 220, 5))
		screen.blit(p2Text, (55, 50))
		screen.blit(winsText, (225, 200))
	elif winner == 3:
		youWinText = font1.render("You win!", True, (250, 220, 5))
		screen.blit(youWinText, (125, 150))
	elif winner == 4:
		youLoseText = font1.render("You lose!", True, (250, 220, 5))
		screen.blit(youLoseText, (125, 150))

#	p1Text = font1.render("Player One", True, (250, 220, 5))
#	p2Text = font1.render("Player Two", True, (250, 220, 5))
#	winsText = font1.render("Wins!", True, (250, 220, 5))
#	youWinsText = font1.render("You Win!", True, (250, 220, 5))
#	youLoseText = font1.render("You lose!", True, (250, 220, 5))
#	font2 = pygame.font.SysFont(font, 60)
#	playAgainText = font2.render("Play Again", True, (250, 220, 5))
#	background = pygame.image.load('board.png')
#	pygame.transform.scale(background, (swidth, sheight), screen)
#	screen.blit(p1Text, (25, 50))
#	screen.blit(winsText, (150, 175))
#	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 400, 300, 100))
#	screen.blit(playAgainText, (190, 425))

	

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	homeScreen(screen)
	resultScreen(4, screen)
	pygame.display.flip
	clock.tick(60)

