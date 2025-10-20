import pygame
import random
from damage_text import DamageText
from config import red, green, font

# Clasa pentru personajele folosite
class Characters():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = [] # Lista mare de animatii
        self.frame_index = 0 # Indexul de pornire al animatiilor
        self.action = 0 # Controleaza animatiile prin numere asignate: 0: Idle, 1: Atac, 2: Ranit, 3: Mort
        self.update_time = pygame.time.get_ticks() # Asigneaza un timp indexului animatiilor

        # Incarcare animatii - Frame-urile difera in functie de personaj + asset-urile se pot modifica
        for action_name in ["Idle", "Attack", "Hurt", "Death"]:
            temp_list = []
            i = 0
            while True:
                try:
                    img = pygame.image.load(f"Graphics/{self.name}/{action_name}/{i}.png").convert_alpha() # F strings usureaza munca
                    img = pygame.transform.scale(img, (img.get_width() * 5, img.get_height() * 5)) # Mareste imaginile si animatiile
                    temp_list.append(img)
                    i += 1
                except (pygame.error, FileNotFoundError):
                    break # Loop-ul se opreste din incarcat frame-uri noi cand ramane fara fisiere de animatie in folder
            self.animation_list.append(temp_list) # Adauga temp_list la animation_list si creste self.action cu 1

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect() # Creaza un patrat-imagine care poate fi pozitionat pe ecran
        self.rect.center = (x, y) # Coordonatele la care va fi pozitionat patratul


    def update(self): # Ruleaza animatiile
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index] # Updateaza animatiile
        # Verifica daca a trecut destul timp de la ultimul update de animatie
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
        # Daca diferenta dintre timpul curent minus ultimul update este mai mare de 100 ms, updateaza animatia
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]): # Reia animatiile de la 0 cand se termina fisierele
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1 # Animatia ramane pe Death daca moare personajul
            elif self.action in [1, 2]:
                self.idle() # Intoarce animatia pe Idle doar dupa ce se termina animatiile de Attack sau Hurt
            else:
                self.frame_index = 0 # Loop-uie animatia de Idle

    def idle(self): # Animatia Idle
        self.action = 0 # Revine la animatia de Idle dupa ce a avut loc o alta actiune
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target, damage_text_group): # Permite personajelor sa atace
        rand = random.randint (-5, 5) # Variaza o parte damage-ul personajelor
        damage = self.strength + rand
        target.hp -= damage
        target.hurt() # Ruleaza animatia Hurt cand cineva este atacat
        if target.hp < 1: # Verifica daca a murit un personaj
            target.hp = 0
            target.alive = False
            target.death() # Ruleaza animatia Death cand personajul moare
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red) # Instanta pentru damage text
        damage_text_group.add(damage_text)
        self.action = 1 # Schimba animatia la cea de atac cand actiunea are loc
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self): # Animatia Hurt
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self): # Animatia Death
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, screen): # Aseaza si arata grafica personajelor
        screen.blit(self.image, self.rect) # Patratul "rect" preia proprietatile imaginii