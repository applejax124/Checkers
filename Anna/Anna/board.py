#!/~pbui/pub/anaconda2-4.1.1/bin/python

#move checkers piece between squares

import pygame

pygame.init() #initialize all pygame modules
screen = pygame.display.set_mode((400, 400)) #open 400x400 window
play = True
clock = pygame.time.Clock()

#draw initial board squares
pygame.draw.rect(screen,(250,0,0),pygame.Rect(75,200,50,50))
pygame.draw.rect(screen,(0,0,250),pygame.Rect(275,200,50,50))

while (play):
   for event in pygame.event.get():
      if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
      #if r key pressed, place circle in red box
         screen.fill((0,0,0))
	 pygame.draw.rect(screen,(250,0,0),pygame.Rect(75,200,50,50))
         pygame.draw.rect(screen,(0,0,250),pygame.Rect(275,200,50,50))
         pygame.draw.circle(screen,(250,250,250),(100,225),20)
      if event.type==pygame.KEYDOWN and event.key==pygame.K_b:
      #if b key pressed, place circle in blue box
	 screen.fill((0,0,0))
         pygame.draw.rect(screen,(250,0,0),pygame.Rect(75,200,50,50))
         pygame.draw.rect(screen,(0,0,250),pygame.Rect(275,200,50,50))
         pygame.draw.circle(screen,(250,250,250),(300,225),20)
      if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
      #if space button pressed, quit screen
         play = False

      clock.tick(60)
      pygame.display.flip()


