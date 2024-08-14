import pygame
from data import FONT1, RED, WHITE
pygame.init()

# money bars
class MoneyBar:
    def __init__(self, x, y, image, amount):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.amount = amount
        self.revealed = False 

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        
        color = RED if self.revealed else WHITE
        text = FONT1.render(self.amount, True, color)
        
        text_rect = text.get_rect(center=(self.rect.x + self.image.get_width() // 2 + 16, 
                                          self.rect.y + self.image.get_height() // 2))
        
        surface.blit(text, text_rect)

    def reveal(self):
        self.revealed = True

    def is_match(self, prize):
        return self.amount == prize
