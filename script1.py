retry = 0
dotcount = 0
level = 0
countdown = 40
subtime = 0
a = 0
bombx = []
dropsx = []
dropsy = []
(drops, gy,) = (0, 0)
import pygame
import random
import time
import math
from pygame.locals import *
pygame.init()
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % ((pygame.display.Info().current_w-1366)/2, (pygame.display.Info().current_h-768)/2)
pygame.quit()
pygame.init()
pygame.event.pump()
screen = pygame.display.set_mode((1366, 768), pygame.NOFRAME)
tickrate = 31
try:
    logo = pygame.image.load('Down Down Dead logo.png').convert()
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Down Down Dead!', 'Down Down Dead logo.png')
except:
    pass
gx = random.randint(int(0), int(screen.get_width()))
pygame.event.pump()


text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Press 1, 2 or 3 to select difficulty', 0, (50, 255, 50))
textpos = text.get_rect()
textpos.centerx = screen.get_width() / 2
textpos.centery = screen.get_height() / 2
screen.blit(text, textpos)
pygame.display.update()
pygame.mouse.set_visible(False)
try:
    while True:
        a = 0
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    tickrate = tickrate * 3
                    diff = 0.5
                    raise SystemExit
                elif event.key == K_2:
                    diff = 1
                    raise SystemExit
                elif event.key == K_3:
                    tickrate = tickrate / 2
                    diff = 2
                    raise SystemExit
except SystemExit:
    screen.fill((0,0,0))

text = pygame.font.Font(pygame.font.match_font('comicsansms'), 25).render('This game is coded by Penn Mackintosh and distributed under the latest version of the GNU GPL', 0, (50, 255, 50))
textpos = text.get_rect()
textpos.centerx = screen.get_width() / 2
textpos.centery = screen.get_height() / 2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(2)
pygame.event.pump()
screen.fill((0, 0, 0))
dropcounttext = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(dotcount), 0, (50, 255, 50))
counttext = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('40', 0, (50, 255, 50))
t1 = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('3', 0, (50, 255, 50))
t2 = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('2', 0, (50, 255, 50))
t3 = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('1', 0, (50, 255, 50))
LEVELUP = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('LEVEL UP', 0, (50, 255, 50))
ENDGAME = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('END GAME', 0, (50, 255, 50))
QUITI = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('ESCAPE TO QUIT', 0, (50, 255, 50))
text = QUITI
textpos = text.get_rect()
textpos.centerx = screen.get_width() / 2
textpos.centery = screen.get_height() / 2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
screen.fill((0, 0, 0))
text = t1
textpos = text.get_rect()
textpos.centerx = screen.get_width() / 2
textpos.centery = screen.get_height() / 2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
pygame.event.pump()
screen.fill((0, 0, 0))
text = t2
textpos = text.get_rect()
textpos.centerx = screen.get_width() / 2
textpos.centery = screen.get_height() / 2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
pygame.event.pump()
screen.fill((0, 0, 0))
text = t3
textpos = text.get_rect()
textpos.centerx = screen.get_width() / 2
textpos.centery = screen.get_height() / 2
screen.blit(text, textpos)
pygame.display.update()
time.sleep(1)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
REGEN = USEREVENT + 1
UPLEVEL = USEREVENT + 2
pygame.time.set_timer(REGEN, 1000)
pygame.time.set_timer(UPLEVEL, 40000)
activeevent = False
starttime = time.time()
try:
    while True:
        pygame.mouse.set_visible(False)
        a = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                subtime += 2
                text = ENDGAME
                textpos = text.get_rect()
                textpos.centerx = screen.get_width() / 2
                textpos.centery = screen.get_height() / 2
                screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(2)
                screen.fill((0, 0, 0))
                text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(time.time() - starttime - subtime/diff), 0, (50, 255, 50))
                textpos = text.get_rect()
                textpos.centerx = screen.get_width() / 2
                textpos.centery = screen.get_height() / 2
                screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(2)
                
                pygame.quit()
                raise SystemExit
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    subtime += 2
                    text = ENDGAME
                    textpos = text.get_rect()
                    textpos.centerx = screen.get_width() / 2
                    textpos.centery = screen.get_height() / 2
                    screen.blit(text, textpos)
                    pygame.display.update()
                    time.sleep(2)
                    screen.fill((0, 0, 0))
                    text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(time.time() - starttime - subtime/diff), 0, (50, 255, 50))
                    textpos = text.get_rect()
                    textpos.centerx = screen.get_width() / 2
                    textpos.centery = screen.get_height() / 2
                    screen.blit(text, textpos)
                    pygame.display.update()
                    time.sleep(2)
                    
                    pygame.quit()
                    raise SystemExit
            elif event.type == REGEN:
                dropsx.append(random.randint(int(0), int(screen.get_width() / 20)))
                dropsy.append(screen.get_height() / 20)
                drops += 1
                bombx.append(random.randint(int(0), int(screen.get_width() / 20)))
                counttext = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(countdown), 0, (50, 255, 50))
                textpos = text.get_rect()
                screen.blit(counttext, (0, 0))
                pygame.display.update()
                countdown -= 1
            elif event.type == UPLEVEL:
                if dotcount >= 10:
                    subtime += 2
                    tickrate -= 2
                    level += 1
                    text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('Level: ' + str(level) + ' Speed: ' + str(tickrate), 0, (50, 255, 50))
                    textpos = text.get_rect()
                    textpos.centerx = screen.get_width() / 2
                    textpos.centery = screen.get_height() / 2
                    screen.blit(text, textpos)
                    pygame.display.update()
                    time.sleep(2)
                    retry = 0
                elif retry == 0:
                    subtime += 42
                    tickrate -= 2
                    level += 1
                    text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('RETRY: Get More Dots To Pass Level: ' + str(level) + ' Speed: ' + str(tickrate), 0, (50, 255, 50))
                    textpos = text.get_rect()
                    textpos.centerx = screen.get_width() / 2
                    textpos.centery = screen.get_height() / 2
                    screen.blit(text, textpos)
                    pygame.display.update()
                    time.sleep(2)
                    retry = 1
                else:
                    subtime += 2
                    text = ENDGAME
                    textpos = text.get_rect()
                    textpos.centerx = screen.get_width() / 2
                    textpos.centery = screen.get_height() / 2
                    screen.blit(text, textpos)
                    pygame.display.update()
                    time.sleep(2)
                    screen.fill((0, 0, 0))
                    text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(time.time() - starttime - subtime/diff), 0, (50, 255, 50))
                    textpos = text.get_rect()
                    textpos.centerx = screen.get_width() / 2
                    textpos.centery = screen.get_height() / 2
                    screen.blit(text, textpos)
                    pygame.display.update()
                    time.sleep(2)
                    
                    pygame.quit()
                    raise SystemExit
                counttext = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('40', 0, (50, 255, 50))
                countdown = 40
                dotcount = 0
                dropcounttext = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render('0', 0, (50, 255, 50))
            elif event.type == ACTIVEEVENT:
                if event.gain == 0:
                    while True:
                        pygame.mouse.set_visible(True)
                        newevent = pygame.event.poll()
                        if newevent.type == QUIT:
                            subtime += 2
                            text = ENDGAME
                            textpos = text.get_rect()
                            textpos.centerx = screen.get_width() / 2
                            textpos.centery = screen.get_height() / 2
                            screen.blit(text, textpos)
                            pygame.display.update()
                            time.sleep(2)
                            screen.fill((0, 0, 0))
                            text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(time.time() - starttime - subtime/diff), 0, (50, 255, 50))
                            textpos = text.get_rect()
                            textpos.centerx = screen.get_width() / 2
                            textpos.centery = screen.get_height() / 2
                            screen.blit(text, textpos)
                            pygame.display.update()
                            time.sleep(2)
                            
                            pygame.quit()
                            raise SystemExit
                        elif newevent.type == ACTIVEEVENT:
                            if newevent.gain == 1:
                                pygame.mouse.set_visible(False)
                                break
                        time.sleep(1)
                        subtime += 1


        screen.fill((0, 0, 0))
        (x, y,) = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 0, 0), (int(x / 20) * 20,
         int(y / 20) * 20,
         20,
         20), 0)
        while a < drops:
            pygame.draw.rect(screen, (200, 200, 200), (dropsx[a] * 20,
             dropsy[a] * 20,
             20,
             20), 0)
            dropsy[a] -= 0.025 * (1000.0 / tickrate / clock.get_time())
            if [dropsx[a] * 20, round(dropsy[a]) * 20] == [int(x / 20) * 20, int(y / 20) * 20]:
                gx = dropsx[a] * 20
                gy = dropsy[a] * 20
                dotcount += 1
                dropcounttext = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(dotcount), 0, (50, 255, 50))
                dropsy.pop(a)
                dropsx.pop(a)
                drops -= 1
            a += 1

        a = 0
        while a < drops:
            pygame.draw.rect(screen, (0, 0, 200), (bombx[a] * 20,
             dropsy[a] * 20,
             20,
             20), 0)
            try:
                gy += 0.075 * (1000.0 / tickrate / clock.get_time())
            except ZeroDivisionError:
                try:
                    dropsy[a] += 0.075 / tickrate
                    bomby[a] += 0.075 / tickrate
                except ZeroDivisionError:
                    dropsy[a] += 0.075
                    bomby[a] += 0.075
            if [bombx[a] * 20, round(dropsy[a]) * 20] == [int(x / 20) * 20, int(y / 20) * 20]:
                subtime += 2
                text = ENDGAME
                textpos = text.get_rect()
                textpos.centerx = screen.get_width() / 2
                textpos.centery = screen.get_height() / 2
                screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(2)
                screen.fill((0, 0, 0))
                text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(time.time() - starttime - subtime/diff), 0, (50, 255, 50))
                textpos = text.get_rect()
                textpos.centerx = screen.get_width() / 2
                textpos.centery = screen.get_height() / 2
                screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(2)
                
                pygame.quit()
                raise SystemExit
            a += 1

        try:
            gy += 0.045 * (1000.0 / tickrate / clock.get_time())
        except ZeroDivisionError:
            gy += 0.455 / (1000.0 / tickrate)
        if gy >= screen.get_height():
            subtime += 2
            text = ENDGAME
            textpos = text.get_rect()
            textpos.centerx = screen.get_width() / 2
            textpos.centery = screen.get_height() / 2
            screen.blit(text, textpos)
            pygame.display.update()
            time.sleep(2)
            screen.fill((0, 0, 0))
            text = pygame.font.Font(pygame.font.match_font('comicsansms'), 55).render(str(time.time() - starttime - subtime/diff), 0, (50, 255, 50))
            textpos = text.get_rect()
            textpos.centerx = screen.get_width() / 2
            textpos.centery = screen.get_height() / 2
            screen.blit(text, textpos)
            pygame.display.update()
            time.sleep(2)
            
            pygame.quit()
            raise SystemExit
        screen.blit(counttext, (0, 0))
        screen.blit(dropcounttext, (screen.get_width() - dropcounttext.get_width(), 0))
        pygame.draw.rect(screen, (0, 255, 0), (gx, gy, 20, 20), 0)
        clock.tick(0)
        pygame.display.update()

except SystemExit:
    import StartGame
    pass

