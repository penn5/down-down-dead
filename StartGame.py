import pygame
import random
import time
import sys
print 'hello'
from pygame.locals import *
print 'hello'
pygame.quit()
pygame.init()
print 'hello'
pygame.event.pump()
print 'hello'
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
print 'hello'
pygame.font.init()
print pygame.font.match_font('comicsansms')
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Start', 0, (50, 255, 50), (20, 20, 20))
print 'hello'
(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Start')
print 'hello'
textpos = text.get_rect()
print 'hello'
textpos.centerx = screen.get_width() / 2
print 'hello'
textpos.centery = screen.get_height() / 2
print 'hello'
screen.blit(text, textpos)
print 'hello'
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
                    raise RuntimeError('Programmer Error - script1 exited with an error - please report to penn.mackintosh@gmail.com')
                pygame.quit()
                sys.exit()
            if x > instrpos.centerx - instrx / 2 and x < instrpos.centerx + instrx / 2 and y > instrpos.centery - instry / 2 and y < instrpos.centery + instry / 2:
                try:
                    import script2
                except Exception:
                    raise RuntimeError('Programmer Error - script2 exited with an error - please report to penn.mackintosh@gmail.com')
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()



