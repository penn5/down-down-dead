import pygame
import random
import time
import sys
from pygame.locals import *
import os
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
xoff = abs(screen.get_width() - 1366)/2
yoff = abs(screen.get_height() - 768)/2
try:
    logo = pygame.image.load('Down Down Dead logo.png').convert()
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Down Down Dead!', 'Down Down Dead logo.png')
except:
    pass
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Avoid the blue dots', 0, (50, 255, 50))
(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Avoid the blue dots')
textpos = text.get_rect()
textpos.centerx = (screen.get_width()+xoff) / 2
textpos.centery = (screen.get_height()+yoff) / 2
screen.blit(text, textpos)
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Catch the white dots as late as possible', 0, (50, 255, 50))
(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Catch the white dots as late as possible')
textpos = text.get_rect()
textpos.centerx = (screen.get_width()+xoff) / 2
textpos.centery = (screen.get_height()+yoff) / 2 - 55
screen.blit(text, textpos)
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Keep the green dot high', 0, (50, 255, 50))
(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Keep the green dot high')
textpos = text.get_rect()
textpos.centerx = (screen.get_width()+xoff) / 2
textpos.centery = (screen.get_height()+yoff) / 2 - 110
screen.blit(text, textpos)
text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Start', 0, (50, 255, 50), (20, 20, 20))
(startx, starty,) = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).size('Start')
textpos = text.get_rect()
textpos.centerx = (screen.get_width()+xoff) / 2
textpos.centery = (screen.get_height()+yoff) / 2 - 165
screen.blit(text, textpos)
pygame.display.update()
try:
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                (x, y,) = pygame.mouse.get_pos()
                if x > textpos.centerx - startx / 2 and x < textpos.centerx + startx / 2 and y > textpos.centery - starty / 2 and y < textpos.centery + starty / 2:
                    import script1
                    raise SystemExit


except SystemExit:
    pass
