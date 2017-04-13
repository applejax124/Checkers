#/afs/nd.edu/user14/csesoft/cse20312/bin/python
#!~pbui/pub/anaconda2-4.1.1/bin

import pygame

def board():
   colorAlt = 0
   for x in range (52,748,87):
      colorAlt+=1
      for y in range (52,748,87):
	 if (colorAlt % 2 == 0): color = (255,0,0)
	 else: color = (0,0,255)
         pygame.draw.rect(screen,color,pygame.Rect(x,y,87,87))
	 colorAlt+=1

pygame.init()
screen = pygame.display.set_mode((800,800))
play = True
clock = pygame.time.Clock()

board()

while (play):
   for event in pygame.event.get():
      if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
	 print pygame.mouse.get_pos()
	 screen.fill((0,0,0))
	 board()
	 pygame.draw.circle(screen,(255,255,255),pygame.mouse.get_pos(),20)
      #if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
	 #print "HEY!"
      if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
         play = False

      #clock.tick(60)
      pygame.display.flip()

