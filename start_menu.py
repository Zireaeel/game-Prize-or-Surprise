from data import *

def start_screen():
    pygame.display.set_caption("Prize or Surprise - Start Screen")
    start_music.play()
    
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_effect.play()
                    start_music.stop()
                    pygame.time.wait(1600)
                    running = False
        
        screen.blit(start_background_bg, (0, 0))
        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Prize or Surprise - Main Menu")
    action_thrilling_music.play(-1)

    start_time = pygame.time.get_ticks()
    zireaeel_yazi_gorunme = False
    dark_scratch_yazi_gorunme = False
    winning_effect_played1 = False
    winning_effect_played2 = False
    game_paused = False
    menu_state = "main"

    made_by_zireaeel_yazi = FONT4.render("made by Zireaeel", True, GRAY)
    made_by_zireaeel_yazi_koordinat = made_by_zireaeel_yazi.get_rect()
    made_by_zireaeel_yazi_koordinat.topleft = (600,10)

    #oyun döngüsü, main loop
    run = True
    while run:
        screen.blit(main_menu1_bg, (0,0))

        if zireaeel_yazi_gorunme:
            screen.blit(made_by_zireaeel_yazi, made_by_zireaeel_yazi_koordinat)
            if not winning_effect_played1:
                winning_effect.play()
                winning_effect_played1 = True
        if pygame.time.get_ticks() - start_time >= 11000:    #11000 milisaniye = 11 seconds
            zireaeel_yazi_gorunme = True

        if home_button.draw(screen):
            if game_paused:
                menu_state = "main"
                game_paused = False
            else:
                game_paused = True

        if game_paused == True:
            if menu_state == "main":
                draw_text("Will you go home a millionaire or empty-handed?", FONT1, DARK_WHITE, 219.5, 560)
                if resume_button.draw(screen):
                    game_paused = False
                if options_button.draw(screen):
                    menu_state = "options"
            if menu_state == "options":
                if settings_button.draw(screen):
                    menu_state = "settings"
                if controls_button.draw(screen):
                    menu_state = "controls"
                if back_button.draw(screen):
                    menu_state = "main"
            if menu_state == "settings":
                draw_text("Sound", FONT4, WHITE, 247, 190)
                draw_text("Resolution           1024 x 636", FONT4, WHITE, 194, 290)
                if left_button.draw(screen):
                    action_thrilling_music.set_volume(0.1)
                if right_button.draw(screen):
                    action_thrilling_music.set_volume(0.3)
                if back_button.draw(screen):
                    menu_state = "options"
            if menu_state == "controls":
                draw_text("""
                  The player chooses suitcases numbered 1 to 20. At the end,
                the player takes the unopened suitcase. The banker offers a
                   deal based on opened suitcases. The player can accept the
                    deal or keep the unopened suitcase for the grand prize.
                """, FONT1, DARK_WHITE, 28, 165)
                draw_text("Mouse left click:  Allows you to select and open suitcases.", FONT1, DARK_WHITE, 156, 126)
                if back_button.draw(screen):
                    menu_state = "options"

        else:
            if dark_scratch_yazi_gorunme:
                draw_text("Prize  or  Surprise", FONT4, TURQOISE, 290.5, 290)
                if not winning_effect_played2:
                    winning_effect.play() 
                    winning_effect_played2 = True
            if pygame.time.get_ticks() - start_time >= 1000:    #1000 milisaniye = 1 saniye
                dark_scratch_yazi_gorunme = True
            if start_button.draw(screen):
                game_started_effect.play()
                action_thrilling_music.stop()
                pygame.time.wait(2000)
                run = False
            if quit_button.draw(screen):
                exit_effect.play()
                action_thrilling_music.stop()
                pygame.time.wait(1000)
                run = False
                exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

def normal_game_ending(suitcase_number, prize):
    run = True
    while run:
        screen.blit(background2, (0, 0))
        screen.blit(dialogue_IMG, (70, 100))
        draw_text(f"You chose suitcase {suitcase_number}", FONT2, BLACK, 210, 160)
        draw_text("You won", FONT3, DARK_COFFEE, 310, 205)
        screen.blit(dollar_IMG, (190, 255))
        draw_text(f"${prize}", FONT4, DARK_GREEN, 270, 250)
        screen.blit(presenter3_IMG, (685, 110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    exit()

