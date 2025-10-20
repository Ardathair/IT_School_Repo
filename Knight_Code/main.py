import pygame
import config
from menu import show_main_menu
from characters import Characters
from healthbar import HealthBar
from damage_text import DamageText
import button


pygame.init()


# Variabila menita sa limiteze FPS-ul aplicatiei
clock = pygame.time.Clock()
# Limita de FPS
fps = 60


# Initializeaza ecranul de joc
screen_width = config.screen_width
screen_height = config.screen_height
bottom_panel = config.bottom_panel

screen = pygame.display.set_mode((config.screen_width, config.screen_height))

font = config.font
big_font = config.big_font
red = config.red
green = config.green
# Numele ferestrei aplicatiei
pygame.display.set_caption("KnightFight")


# Meniul Principal
show_main_menu(screen, font, big_font, screen_width, screen_height, red, green)


# Muzica
pygame.mixer.music.load("Music/combat_track.wav")
victory_sound = pygame.mixer.Sound("Music/victory_track.wav")
defeat_sound = pygame.mixer.Sound("Music/defeat_track.wav")

music_ended = False # Previne overlap-ul pentru muzica

pygame.mixer.music.set_volume(0.8) # Volum pentru combat music
victory_sound.set_volume(0.8) # Volum pentru victory music
defeat_sound.set_volume(1.0) # Volum pentru defeat music


# Grafica

# Imaginea de fundal din lupta
background_image = pygame.image.load("Graphics/Background/background.png").convert_alpha()

# Grafica ecranului de statistici
panel_image = pygame.image.load("Graphics/Icons/panel.png").convert_alpha()

# Iconita pentru potiuni
potion_image = pygame.image.load("Graphics/Icons/potion.png").convert_alpha()

# Imaginea cursorului
sword_image = pygame.image.load("Graphics/Icons/cursor.png").convert_alpha()
# Marim cursorul
sword_image = pygame.transform.scale(sword_image, (sword_image.get_width() * 2, sword_image.get_height() * 2))

def draw_text(text, font, text_col, x, y): # Preia text si-l converteste intr-o imagine (Pygame nu poate afisa text)
    img = font.render(text, True, text_col) # "True" este pentru text antialiasing
    screen.blit(img, (x, y))

def draw_bg(): # Aseaza si arata imaginea de fundal din lupta
    screen.blit(background_image, (0, 0))

def draw_panel(MC, bandit_list): # Aseaza si arata imaginea ecranului de statistici
    screen.blit(panel_image, (0, screen_height - bottom_panel))
    # Statisticile personajului principal
    draw_text(f"{MC.name} HP: {MC.hp}", font, red, 280, screen_height - bottom_panel + 35)
    # Statisticile inamicilor
    for count, i in enumerate(bandit_list):
        draw_text(f"{i.name} HP: {i.hp}", font, red, 1030, (screen_height - bottom_panel + 35) + count * 120)


# Buton potiuni
potion_button = button.Button(screen, 335, screen_height - bottom_panel + 150, potion_image, 120, 120)


# Variabile pentru gameplay
action_cooldown = 0
action_wait_time = 90
potion_effect = 20
clicked = False # Verifica daca jucatorul a dat click pe mouse
game_over = 0 # Folosim -1, 0 si 1 pentru a diferentia intre Win si Lose la sfarsitul jocului


# Damage text
damage_text_group = pygame.sprite.Group()


# Game restart
def reset_game():
    global MC, HB, LB, bandit_list
    global MC_health_bar, HB_health_bar, LB_health_bar
    global damage_text_group
    global current_character, action_cooldown, clicked, game_over, music_ended
    global action_wait_time, potion_effect, total_characters


    # Personaje
    # Avem grija ca "self.name" sa fie identic cu numele folderului, ca sa profitam de f string-ul introdus
    MC = Characters(395, 720, "Knight", 30, 10, 3) # Personaj principal
    HB = Characters(1073, 740, "Heavy Bandit", 30, 6, 1) # Inamic I
    LB = Characters(1336, 740, "Light Bandit", 20, 6, 0) # Inamic II

    bandit_list = [] # Creaza o lista cu inamici pentru iterare
    bandit_list.append(HB)
    bandit_list.append(LB)


    # Bari de HP
    MC_health_bar = HealthBar(270, screen_height - bottom_panel + 100, MC.hp, MC.max_hp) # Personaj principal
    HB_health_bar = HealthBar(1080, screen_height - bottom_panel + 100, HB.hp, HB.max_hp) # Inamic I
    LB_health_bar = HealthBar(1080, screen_height - bottom_panel + 220, LB.hp, LB.max_hp) # Inamic II

    # Reset variabile
    current_character = 1
    total_characters = 3
    action_cooldown = 0
    game_over = 0
    music_ended = False


    damage_text_group.empty()  # Curata textul de pe ecran


    # Restarteaza muzica
    pygame.mixer.stop()  # Opreste sunetele
    pygame.mixer.music.stop()  # Opreste muzica
    pygame.mixer.music.play(-1)  # Restarteaza muzica si o pune inapoi in loop


# Re-initializeaza setup-ul
reset_game()


# Main loop
run = True
cursor_visible = True
while run:

    clock.tick(fps) # Limita de FPS, activa cat ruleaza loop-ul

    draw_bg() # Imaginea de fundal din lupta, activa cat ruleaza loop-ul
    draw_panel(MC, bandit_list) # Grafica ecranului de statistici, activa cat ruleaza loop-ul
    MC_health_bar.draw(screen, MC.hp) # Grafica pentru barile de HP
    HB_health_bar.draw(screen, HB.hp)
    LB_health_bar.draw(screen, LB.hp)

    MC.update()
    MC.draw(screen) # Grafica pentru personajul principal
    for bandit in bandit_list: # Grafica pentru inamici
        bandit.update()
        bandit.draw(screen)

    damage_text_group.update()
    damage_text_group.draw(screen) # Grafica pentru damage text

    # Actiunile jucatorului
    # Variabilele sunt inactive pana la interventia jucatorului
    attack = False
    potion = False
    target = None

    # Mouse logic
    should_show_cursor = True # Cursorul e vizibil daca nu target-uie un inamic
    pos = pygame.mouse.get_pos() # Verifica pozitia cursorului
    for bandit in bandit_list: # Schimba cursorul mouse-ului cu grafica Custom cand target-ul este un inamic
        if bandit.rect.collidepoint(pos) and bandit.alive:
            should_show_cursor = False
            screen.blit(sword_image, pos)
            if clicked: # Permite atacarea inamicilor cu mouse-ul
                attack = True
                target = bandit

    if should_show_cursor != cursor_visible: # Schimba vizibilitatea cursorului doar daca a fost schimbat de la ult frame
        pygame.mouse.set_visible(should_show_cursor)
        cursor_visible = should_show_cursor

    # Potion Button
    if potion_button.draw():
        potion = True
    draw_text(str(MC.potions), font, red, 425, screen_height - bottom_panel + 155) # Arata nr de potiuni ramase

    # Actiunile jucatorului
    if game_over == 0:
        if MC.alive:
            if current_character == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack and target: # Atac
                        MC.attack(target, damage_text_group)
                        current_character += 1
                        action_cooldown = 0 # Reia atacul cand revine randul jucatorului
                    if potion and MC.potions > 0 and MC.hp < MC.max_hp: # Refacere HP daca MC are potiuni si nu este full HP
                        heal_amount = min(potion_effect, MC.max_hp - MC.hp) # Potiunea nu trebuie sa depaseasca Max HP
                        MC.hp += heal_amount
                        MC.potions -= 1 # Scade o potiune
                        damage_text = DamageText(MC.rect.centerx, MC.rect.y, str(heal_amount), green) # Text pentru heal
                        damage_text_group.add(damage_text)
                        current_character += 1 # Trece la personajul urmator
                        action_cooldown = 0
        else:
            game_over = -1

        # Actiunile inamicilor
        for count, bandit in enumerate(bandit_list):
            if current_character == 2 + count:
                if bandit.alive:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        if bandit.hp / bandit.max_hp <= 0.5 and bandit.potions > 0: # Refacere HP daca este sub 50%
                            heal_amount = min(potion_effect, bandit.max_hp - bandit.hp)
                            bandit.hp += heal_amount
                            bandit.potions -= 1
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green) # Text pentru heal
                            damage_text_group.add(damage_text)
                        else:
                            bandit.attack(MC, damage_text_group) # Atac
                        current_character += 1
                        action_cooldown = 0
                else:
                    current_character += 1 # Daca inamicul moare, nu mai ataca

        if current_character > total_characters: # Trece la urmatoarea "runda" odata ce toata lumea a atacat
            current_character = 1

    # Verifica daca mai sunt inamici in viata
    alive_bandits = sum(1 for b in bandit_list if b.alive)
    if alive_bandits == 0:
        game_over = 1

    # Game Over
    if game_over != 0 and not music_ended: # Initializeaza muzica de Game Over
        pygame.mixer.music.stop()
        if game_over == 1:
            victory_sound.play()
        else:
            defeat_sound.play()
        music_ended = True

    # Game Over texts
    if game_over == 1:
        draw_text("You are Victorious!", big_font, green, screen_width // 2 - 579, 200)
        draw_text("Press any key to restart", font, red, screen_width // 2 - 200, 400)
    elif game_over == -1:
        draw_text("You've been Defeated!", big_font, red, screen_width // 2 - 674, 200)
        draw_text("Press any key to restart", font, red, screen_width // 2 - 200, 400)

    # Quit
    clicked = False
    for event in pygame.event.get(): # Ii permite user-ului sa opreasca loop-ul
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Detecteaza butonul apasat de la mouse
            clicked = True
        elif event.type == pygame.KEYDOWN and game_over != 0:  # Detecteaza tasta pentru restart
            reset_game()

    pygame.display.update()


pygame.quit()