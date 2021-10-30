from tonegen import ToneGen
from imageobj import Obj
import textwrap
class Bomb:    
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.ticktimer = 1
        pygame.mixer.music.load('assets/music.ogg')
        pygame.mixer.music.play(-1, 0.0)
        self.lcdtext = ""
        self.explosion = self.pygame.mixer.Sound('assets/bum.ogg')
        self.sprites = []
        self.sprites.append(Obj(pygame.image.load('assets/room.png')))
        self.sprites.append(Obj(pygame.image.load('assets/case.png')))
        self.sprites.append(Obj(pygame.image.load('assets/dynamite.png'), 200, 400))
        xbut = 598
        ybut = 100
        self.sprites.append(Obj(pygame.image.load('assets/lcd.png'), 260, 90))
        button_img = pygame.image.load('assets/button.png')
        buttons = [
        [Obj(button_img, xbut, ybut, "1"), Obj(button_img, xbut + 68, ybut, "2"), Obj(button_img, xbut + 136, ybut, "3")],        
        [Obj(button_img, xbut, ybut + 68, "4"), Obj(button_img, xbut + 68, ybut + 68, "5"), Obj(button_img, xbut + 136, ybut + 68, "6")],      
        [Obj(button_img, xbut, ybut + 136, "7"), Obj(button_img, xbut + 68, ybut + 136, "8"), Obj(button_img, xbut + 136, ybut + 136, "9")],      
        [Obj(button_img, xbut, ybut + 204, "X"), Obj(button_img, xbut + 136, ybut + 204, ">")]
        ]
        for buttonx in buttons:
            for button in buttonx:
                self.sprites.append(button)

    def getevents(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                return False
            elif event.type == self.pygame.MOUSEBUTTONUP:
                pos = self.pygame.mouse.get_pos()
                for sprite in self.sprites:
                    if sprite.rect.collidepoint(pos):
                        if sprite.button:
                            self.buttonpress_handler(sprite.button)

    def buttonpress_handler(self, button):
        print(f"The button {button} was pressed.")
        if button == "X":
            self.lcdtext = ""
        elif button == ">":
            self.lcdtext = str(len(self.lcdtext))
        else:
            self.lcdtext += button

    def beep(self):
        if self.ticktimer >= 1000:
            self.ticktimer = 1000 - self.ticktimer
            ToneGen(self.pygame, 1000, 1000, 0.2)

    def drawstuff(self):
        self.screen.fill((0,0,0))
        for sprite in self.sprites:
            sprite.draw(self.screen)
        myfont = self.pygame.font.SysFont('Liberation Mono, Bold', 16)
        lines = textwrap.wrap(self.lcdtext, 23)[-9:]
        ybase = 170
        i = 0
        for line in lines:
            renderedtext = myfont.render(line, False, (0, 0, 0))
            self.screen.blit(renderedtext, (310, ybase + (i * 16)))
            i += 1
        self.pygame.display.flip()