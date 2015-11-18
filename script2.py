import pygame, random, time
from pygame.locals import *
pygame.init()
pygame.event.pump()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
logo = pygame.image.load('Down Down Dead logo.png').convert()
pygame.display.set_icon(logo)
pygame.display.set_caption('Down Down Dead!', 'Down Down Dead logo.png')
text = pygame.font.Font(None, 55).render('Avoid the blue dots', 0, (50,255,50))
startx, starty = pygame.font.Font(None, 55).size('Avoid the blue dots')
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)
height = starty
text = pygame.font.Font(None, 55).render('Catch the white dots as late as possible', 0, (50,255,50))
startx, starty = pygame.font.Font(None, 55).size('Catch the white dots as late as possible')
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = (screen.get_height()/2)-55
screen.blit(text, textpos)
height = starty
text = pygame.font.Font(None, 55).render('Keep the green dot high', 0, (50,255,50))
startx, starty = pygame.font.Font(None, 55).size('Keep the green dot high')
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = (screen.get_height()/2)-110
screen.blit(text, textpos)
height = starty
pygame.display.update()
while True:
    pygame.event.pump()
