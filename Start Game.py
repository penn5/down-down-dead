import pygame, random, time
from pygame.locals import *
pygame.init()
pygame.event.pump()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
logo = pygame.image.load('Down Down Dead logo.png').convert()
pygame.display.set_icon(logo)
pygame.display.set_caption('Down Down Dead!', 'Down Down Dead logo.png')
text = pygame.font.Font(None, 55).render('Start', 0, (50,255,50), (20,20,20))
startx, starty = pygame.font.Font(None, 55).size('Start')
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)

text = pygame.font.Font(None, 55).render('Instructions', 0, (50,255,50), (20,20,20))
instrx, instry = pygame.font.Font(None, 55).size('Instructions')
instrpos = text.get_rect()
instrpos.centerx = screen.get_width()/2
instrpos.centery = screen.get_height()/2+55
screen.blit(text, instrpos)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if x > (textpos.centerx-(startx/2)) and x < (textpos.centerx+(startx/2)) and y > (textpos.centery-(starty/2)) and y < (textpos.centery+(starty/2)):
                import script1
                pygame.quit()
                exit()
            if x > (instrpos.centerx-(instrx/2)) and x < (instrpos.centerx+(instrx/2)) and y > (instrpos.centery-(instry/2)) and y < (instrpos.centery+(instry/2)):
                import script2
