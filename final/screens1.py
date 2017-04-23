#!~pbui/pub/anaconda2-4.1.1/bin

import pygame

pygame.init()
swidth = 600
sheight = 600

screen = pygame.display.set_mode((swidth, sheight))
clock = pygame.time.Clock()
done = False

def homeScreen():
	pygame.font.init()
	#background = pygame.Surface((swidth, sheight))
	#font = "comicsansms"
	font = "forque"
	font1 = pygame.font.SysFont(font, 180)
	checkersText = font1.render("Checkers", True, (250, 220, 5))
	font2 = pygame.font.SysFont(font, 50)
	player1Text = font2.render("One Player", True, (250, 220, 5))
	player2Text = font2.render("Two Players", True, (250, 220, 5))
	font3 = pygame.font.SysFont(font, 40)
	groupText1 = font3.render("Group Members: Cami Carballo", True, (66, 8, 165))
	groupText2 = font3.render("Kendyll, Kraus, Allison Raines, Anna Smith", True, (66, 8, 165))
	background = pygame.image.load('board.png')
	pygame.transform.scale(background, (swidth, sheight), screen)
	#screen.draw.text("Checkers", (25, 50), owidth=1, ocolor=(0, 0, 0))
	screen.blit(checkersText, (15, 50))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(25, 275, 235, 90))
	screen.blit(player1Text, (50, 300))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(325, 275, 245, 90))
	creen.blit(player2Text, (350, 300))
	screen.blit(groupText1, (105, 500))
	screen.blit(groupText2, (5, 550))
	
#pass in results and this will display them based off of that
def resultScreen(winner):
	pygame.font.init()
	font = "forque"
	font1 = pygame.font.SysFont(font, 150)
	font2 = pygame.font.SysFont(font, 60)
	playAgainText = font2.render("Play Again", True, (250, 220, 5))
	background = pygame.image.load('board.png')
	pygame.transform.scale(background, (swidth, sheight), screen)
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 400, 300, 100))
	screen.blit(playAgainText, (190, 425))

	#choose which one based on passed in parameters
	if winner == 1:
		p1Text = font1.render("Player One", True, (250, 220, 5))
		winsText = font1.render("Wins!", True, (250, 220, 5))
		screen.blit(p1Text, (25, 50))
		screen.blit(winsText, (150, 175))
	elif winner == 2:
		p2Text = font1.render("Player Two", True, (250, 220, 5))
		winsText = font1.render("Wins!", True, (250, 220, 5))
		screen.blit(p2Text, (25, 50))
		screen.blit(winsText, (150, 175))
	elif winner == 3:
		youWinText = font1.render("You win!", True, (250, 220, 5))
		screen.blit(youWinText, (85, 150))
	elif winner == 4:
		youLoseText = font1.render("You lose!", True, (250, 220, 5))
		screen.blit(youLoseText, (85, 150))

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

	
<<<<<<< HEAD
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else: 
			#homeScreen()
			resultScreen(3)
		pygame.display.flip
=======
#while not done:
#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			done = True
<<<<<<< HEAD
#	#homeScreen()
#	resultScreen()
#	pygame.display.flip
=======
	#homeScreen()
#	resultScreen(1)
#	pygame.display.flip
>>>>>>> cf004484a8e637193404a3a1063c4d88797b094c
>>>>>>> 3ec2c4de2bd9d1b7b3c94596d1a3d57062f7e19b
