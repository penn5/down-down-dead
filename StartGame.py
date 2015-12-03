import pygame
import random
import time
import sys

from pygame.locals import *
pygame.init()
import os
screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
<<<<<<< HEAD
time.sleep(1)
(x,y) = screen.get_size()
=======
>>>>>>> 72bf8881cb52c7bc0456aa51ad1166c85b6621bf
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % ((screen.get_size()[0]-1366)/2, (screen.get_size()[1]-768)/2)

pygame.quit()
pygame.init()

pygame.event.pump()
tx=1366
ty=768
if x < tx:
    tx=x
if y < ty:
    ty=y
screen = pygame.display.set_mode((tx, ty), pygame.NOFRAME)

pygame.font.init()
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Start', 0, (50, 255, 50), (20, 20, 20))

(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Start')

textpos = text.get_rect()

textpos.centerx = screen.get_width() / 2

textpos.centery = screen.get_height() / 2

screen.blit(text, textpos)

text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Instructions', 0, (50, 255, 50), (20, 20, 20))
(instrx, instry,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Instructions')
instrpos = text.get_rect()
instrpos.centerx = screen.get_width() / 2
instrpos.centery = screen.get_height() / 2 + instry + starty
screen.blit(text, instrpos)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            (x, y,) = pygame.mouse.get_pos()
            if x > textpos.centerx - startx / 2 and x < textpos.centerx + startx / 2 and y > textpos.centery - starty / 2 and y < textpos.centery + starty / 2:
                try:
                    import script1
                except Exception:
                    pass
                pygame.quit()
                sys.exit()
            if x > instrpos.centerx - instrx / 2 and x < instrpos.centerx + instrx / 2 and y > instrpos.centery - instry / 2 and y < instrpos.centery + instry / 2:
                try:
                    import script2
                except Exception:
                    pass
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()



