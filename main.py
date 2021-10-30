import pygame
from bomb import Bomb
pygame.init()
pygame.mixer.pre_init(44100, 16, 2)
pygame.font.init()
size = (824, 674)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("BOH(Brunova Osobna Hra)")
running = True
clock = pygame.time.Clock()

bomb = Bomb(pygame, screen)

while True:

    bomb.drawstuff()
    
    bomb.ticktimer += clock.tick(60)
    bomb.beep()
    if bomb.getevents() == False:
        break
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()