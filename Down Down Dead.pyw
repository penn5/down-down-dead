# -*- coding: cp1252 -*-
subtime = 0
a = 0
dropsx = []
dropsy = []
drops, gy = 0,0
import pygame, random, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
tickrate = screen.get_height()/50
logo = pygame.image.load('Down Down Dead logo.png').convert()
pygame.display.set_icon(logo)
pygame.display.set_caption('Down Down Dead!', 'Down Down Dead logo.png')
gx = random.randint(int(0), int(screen.get_width()))
pygame.event.pump()
text = pygame.font.Font(None, 25).render('This game is coded by Penn Mackintosh and distributed under the latest version of the GNU GPL', 0, (50,255,50))
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(2)
pygame.event.pump()
screen.fill((0,0,0))
t1 = pygame.font.Font(None, 55).render('3', 0, (50,255,50))
t2 = pygame.font.Font(None, 55).render('2', 0, (50,255,50))
t3 = pygame.font.Font(None, 55).render('1', 0, (50,255,50))
LEVELUP = pygame.font.Font(None, 55).render('LEVEL UP', 0, (50,255,50))
ENDGAME = pygame.font.Font(None, 55).render('END GAME', 0, (50,255,50))
QUITI = pygame.font.Font(None, 55).render('ESCAPE TO QUIT', 0, (50,255,50))
text = QUITI
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
screen.fill((0,0,0))
text = t1
starttime = time.time()
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
pygame.event.pump()
screen.fill((0,0,0))
text = t2
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
pygame.event.pump()
screen.fill((0,0,0))
text = t3
textpos = text.get_rect()
textpos.centerx = screen.get_width()/2
textpos.centery = screen.get_height()/2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
screen.fill((0,0,0))
clock=pygame.time.Clock()
REGEN = USEREVENT+1
UPLEVEL = USEREVENT + 2
pygame.time.set_timer(REGEN, 1000)
pygame.time.set_timer(UPLEVEL, 40000)
activeevent = False
starttime = time.time()
while True:
    a = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            starttime += 2
            text = ENDGAME
            textpos = text.get_rect()
            textpos.centerx = screen.get_width()/2
            textpos.centery = screen.get_height()/2
            screen.blit(text, textpos)
            pygame.display.update()
            time.sleep(2)
            screen.fill((0,0,0))
            text = pygame.font.Font(None, 55).render(str((time.time()-starttime)-subtime), 0, (50,255,50))
            textpos = text.get_rect()
            textpos.centerx = screen.get_width()/2
            textpos.centery = screen.get_height()/2
            screen.blit(text, textpos)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                starttime += 2
                text = ENDGAME
                textpos = text.get_rect()
                textpos.centerx = screen.get_width()/2
                textpos.centery = screen.get_height()/2
                screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(2)
                screen.fill((0,0,0))
                text = pygame.font.Font(None, 55).render(str((time.time()-starttime)-subtime), 0, (50,255,50))
                textpos = text.get_rect()
                textpos.centerx = screen.get_width()/2
                textpos.centery = screen.get_height()/2
                screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
                exit()
        elif event.type == REGEN:
            dropsx.append(random.randint(int(0), int(screen.get_width()/20)))
            dropsy.append(screen.get_height()/20)
            drops += 1
        elif event.type == UPLEVEL:
            tickrate -= 1
            text = LEVELUP
            textpos = text.get_rect()
            textpos.centerx = screen.get_width()/2
            textpos.centery = screen.get_height()/2
            screen.blit(text, textpos)
            pygame.display.update()
            time.sleep(2)
            subtime -= 2
        elif event.type == ACTIVEEVENT:

            if event.gain == 0:
                while True:
                    newevent = pygame.event.poll()
                    if newevent.type == QUIT:
                        starttime += 2
                        text = ENDGAME
                        textpos = text.get_rect()
                        textpos.centerx = screen.get_width()/2
                        textpos.centery = screen.get_height()/2
                        screen.blit(text, textpos)
                        pygame.display.update()
                        time.sleep(2)
                        screen.fill((0,0,0))
                        text = pygame.font.Font(None, 55).render(str((time.time()-starttime)-subtime), 0, (50,255,50))
                        textpos = text.get_rect()
                        textpos.centerx = screen.get_width()/2
                        textpos.centery = screen.get_height()/2
                        screen.blit(text, textpos)
                        pygame.display.update()
                        time.sleep(2)
                        pygame.quit()
                        exit()
                    elif newevent.type == ACTIVEEVENT:
                        if newevent.gain == 1:
                            break
    screen.fill((0,0,0))
    x,y = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (255, 0, 0), ((int((x)/20)*20), (int((y)/20)*20), 20, 20), 0)
    while a < drops:
        pygame.draw.rect(screen, (200,200,200), (dropsx[a]*20, dropsy[a]*20, 20, 20), 0)
        dropsy[a] -= 0.025 * ((1000.000000/tickrate)/clock.get_time())
        if [dropsx[a]*20, round(dropsy[a])*20] == [(int((x)/20)*20), (int((y)/20)*20)]:
            gx = dropsx[a]*20
            gy = dropsy[a]*20
        elif [dropsx[a]*20, round(dropsy[a])*20] == [gx, round(gy/20)*20]:
            starttime += 2
        a += 1
    try:
        gy += 0.05 * ((1000.000000/tickrate)/clock.get_time())
    except ZeroDivisionError:
        gy += 0.05
    if gy >= screen.get_height():
        starttime += 2
        text = ENDGAME
        textpos = text.get_rect()
        textpos.centerx = screen.get_width()/2
        textpos.centery = screen.get_height()/2
        screen.blit(text, textpos)
        pygame.display.update()
        time.sleep(2)
        screen.fill((0,0,0))
        text = pygame.font.Font(None, 55).render(str((time.time()-starttime)-subtime), 0, (50,255,50))
        textpos = text.get_rect()
        textpos.centerx = screen.get_width()/2
        textpos.centery = screen.get_height()/2
        screen.blit(text, textpos)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    pygame.draw.rect(screen, (0,255,0), (gx, gy, 20, 20), 0)
    clock.tick(0)
    pygame.display.update()

