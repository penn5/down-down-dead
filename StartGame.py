import pygame
import random
import time
import sys

from pygame.locals import *
import os
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
xoff = screen.get_width() - 1366
yoff = screen.get_height() - 768

pygame.font.init()
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Start', 0, (50, 255, 50), (20, 20, 20))

(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Start')

textpos = text.get_rect()

textpos.centerx = (screen.get_width()+xoff) / 2

textpos.centery = (screen.get_height()+yoff) / 2

screen.blit(text, textpos)

text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Instructions', 0, (50, 255, 50), (20, 20, 20))
(instrx, instry,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Instructions')
instrpos = text.get_rect()
instrpos.centerx = (screen.get_width()+xoff) / 2
instrpos.centery = (screen.get_height()+yoff) / 2 + instry + starty
screen.blit(text, instrpos)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            (x, y,) = pygame.mouse.get_pos()
            if x > textpos.centerx - startx / 2 and x < textpos.centerx + startx / 2 and y > textpos.centery - starty / 2 and y < textpos.centery + starty / 2:
                import script1
                pygame.quit()
                sys.exit()
            if x > instrpos.centerx - instrx / 2 and x < instrpos.centerx + instrx / 2 and y > instrpos.centery - instry / 2 and y < instrpos.centery + instry / 2:
                import script2
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()



