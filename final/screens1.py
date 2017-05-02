#!~pbui/pub/anaconda2-4.1.1/bin

import pygame
import os

clock = pygame.time.Clock()

def homeScreen(screen):
    pygame.font.init()
    font = "forque"
    font1 = pygame.font.SysFont(font, 230)
    checkersText = font1.render("Checkers", True, (255, 255, 255))
    font2 = pygame.font.SysFont(font, 60)
    player1Text = font2.render("One Player", True, (255, 255, 255))
    player2Text = font2.render("Two Players", True, (255, 255, 255))
    font3 = pygame.font.SysFont(font, 30)
    groupText1 = font3.render("Cami Carballo, Kendyll Kraus, Allison Raines, Anna Smith", True, (192, 192, 192))
    background = pygame.image.load('checkers_game.png')
    background = pygame.transform.scale(background, (800, 800))
    rect = background.get_rect()
    screen.blit(background, rect)
    screen.blit(checkersText, (30, 100))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 425, 300, 120))
    screen.blit(player1Text, (85, 465))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(450, 425, 300, 120))
    screen.blit(player2Text, (475, 465))
    screen.blit(groupText1, (70, 750))
	
#pass in results and this will display them based off of that
def resultScreen(winner, screen):
    pygame.font.init()
    font = "forque"
    font1 = pygame.font.SysFont(font, 185)
    font2 = pygame.font.SysFont(font, 100)
    playAgainText = font2.render("Play Again", True, (255, 255, 255))
    background = pygame.image.load('checkers_game.png')
    background = pygame.transform.scale(background, (800, 800))
    rect = background.get_rect()
    screen.blit(background, rect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 400, 500, 150))
    screen.blit(playAgainText, (225, 440))
    quitText = font2.render("Quit", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(275, 650, 250, 100))
    screen.blit(quitText, (320, 675))

    #choose which one based on passed in parameters
	#1 is red winner, 2 is black winner, 3 is you win, 4 is you lose

    if winner == 1:
        p1Text = font1.render("Red", True, (255, 255, 255))
        winsText = font1.render("Wins!", True, (255, 255, 255))
        screen.blit(p1Text, (275, 50))
        screen.blit(winsText, (225, 200))
    elif winner == 2:
        p2Text = font1.render("Black", True, (255, 255, 255))
        winsText = font1.render("Wins!", True, (250, 255, 255))
        screen.blit(p2Text, (225, 50))
        screen.blit(winsText, (225, 200))
    elif winner == 3:
        youWinText = font1.render("You win!", True, (255, 255, 255))
        screen.blit(youWinText, (125, 150))
    elif winner == 4:
        youLoseText = font1.render("You lose!", True, (255, 255, 255))
        screen.blit(youLoseText, (125, 150))
    else:
        pass

clock.tick(5)	


