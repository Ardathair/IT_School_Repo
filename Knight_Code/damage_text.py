import pygame
from config import font

# Clasa pentru textul de damage si HP healed
class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self) # Mosteneste proprietatile clasei Sprite pentru niste functii pre-coded
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1 # Misca damage text-ul in sus
        self.counter += 1
        if self.counter > 65: # Dupa perioada mentionata, sterge textul
            self.kill()