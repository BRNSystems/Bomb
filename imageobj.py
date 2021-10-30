import pygame
class Obj(pygame.sprite.Sprite):
    def __init__(self, img, x = 0, y = 0, button=""):
        pygame.sprite.Sprite.__init__(self)
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.button = button
        if button:
            myfont = pygame.font.SysFont('Liberation Mono, Bold', 16)
            textsurface = myfont.render(button, False, (0, 0, 0))
            self.image.blit(textsurface, (18, 16))
    def draw(self, screen):
        screen.blit(self.image, self.rect)