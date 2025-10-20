import pygame


def show_main_menu(screen, font, big_font, screen_width, screen_height, red, green):
    menu_bg = pygame.image.load("Graphics/Background/menu.jpg").convert() # Incarca imaginea de fundal
    menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))

    pygame.init()

    # Muzica
    pygame.mixer.music.load("Music/menu_track.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    waiting = True
    clock = pygame.time.Clock()

    while waiting:
        screen.blit(menu_bg, (0, 0)) # Imaginea de fundal

        # Titlul si start prompt-ul
        title_text = big_font.render("KnightFight", True, red)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 150))

        # Prompt
        prompt_text = font.render("Press any key to start", True, red)
        screen.blit(prompt_text, (screen_width // 2 - prompt_text.get_width() // 2, 350))

        # Instructiuni
        instructions_big = font.render("INSTRUCTIONS", True, red)
        instructions_small01 = font.render("Click the enemies to attack them", True, red)
        instructions_small02 = font.render("Click on the potion icon to heal", True, red)
        screen.blit(instructions_big, (screen_width // 2 - instructions_big.get_width() // 2, screen_height - 200))
        screen.blit(instructions_small01, (screen_width // 2 - instructions_small01.get_width() // 2, screen_height - 150))
        screen.blit(instructions_small02, (screen_width // 2 - instructions_small02.get_width() // 2, screen_height - 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
                pygame.mixer.music.stop()

        clock.tick(60) # Limita de FPS