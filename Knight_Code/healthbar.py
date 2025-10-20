import pygame
from config import red, green

# Clasa pentru barile de HP (Hit Points, Health Bar)
class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, screen, hp): # Parametrul "hp" trebuie updatat constant, in functie de cum scade viata personajului
        self.hp = hp # Updateaza punctele de viata
        ratio = self.hp / self.max_hp # Calculeaza procentajul de viata pentru a scadea din bara verde

        pygame.draw.rect(screen, (50, 50, 50), (self.x - 3, self.y - 3, 256, 36)) # Background pentru vizibilitate
        pygame.draw.rect(screen, red, (self.x, self.y, 250, 30)) # Aseaza si arata bara rosie de HP
        pygame.draw.rect(screen, green, (self.x, self.y, 250 * ratio, 30)) # Aseaza si arata bara verde de HP