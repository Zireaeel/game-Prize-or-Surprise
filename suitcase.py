import pygame
from data import FONT1, GRAY  # Import necessary resources
pygame.init()

# suitcases
class Suitcase:
    def __init__(self, x, y, image, scale, number, prize):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.number = number
        self.prize = prize

    def draw(self, surface):
        action = False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        text = FONT1.render(str(self.number), True, GRAY)
        surface.blit(text, (self.rect.x + self.image.get_width() // 2 - text.get_width() // 2, 
                            self.rect.y + self.image.get_height() // 2 - text.get_height() // 2))

        return action
