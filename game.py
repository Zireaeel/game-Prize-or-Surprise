import pygame
import random
import time
from data import *
from moneybar import MoneyBar
from suitcase import Suitcase
from start_menu import start_screen, main_menu

class Game:
    def __init__(self):
        pygame.init()
        self.YUKSEKLIK, self.GENISLIK = YUKSEKLIK, GENISLIK
        self.FPS = FPS
        self.screen = screen
        self.clock = clock

        self.background = self.select_random_background()

        self.initialize_game_objects()

        self.popup_active = False
        self.popup_end_time = 0
        self.suitcases_opened = 0
        self.delay_active = False
        self.delay_end_time = 0
        self.selected_suitcase = None
        self.banker_offer = 0

    def select_random_background(self):
        backgrounds = [background1, background2, background3, background4]
        return random.choice(backgrounds)

    def start_game(self):
        start_screen()
        main_menu()
        self.run()

    def initialize_game_objects(self):
        # Coordinates for suitcases and money bars
        self.coordinates = [(240 + 140 * i, 40) for i in range(4)] + \
                           [(240 + 140 * i, 145) for i in range(4)] + \
                           [(240 + 140 * i, 250) for i in range(4)] + \
                           [(240 + 140 * i, 355) for i in range(4)] + \
                           [(240 + 140 * i, 460) for i in range(4)]

        self.coordinates1 = [(20, 22 + 60 * i) for i in range(10)]
        self.coordinates2 = [(830, 22 + 60 * i) for i in range(10)]

        # Prize amounts
        self.prizes = ["1", "10", "25", "50", "75", "100", "250", "500", "750", "1.000", "2.500", "5.000", "10.000", "25.000", "50.000", "100.000", "250.000", "500.000", "750.000", "1.000.000"]
        random.shuffle(self.prizes)

        # Create Suitcase and MoneyBar objects
        self.money_bars_left = [MoneyBar(x, y, gold_bar_IMG, prize) for (x, y), prize in zip(self.coordinates1, ["1", "10", "25", "50", "75", "100", "250", "500", "750", "1.000"])]
        self.money_bars_right = [MoneyBar(x, y, gold_bar_IMG, prize) for (x, y), prize in zip(self.coordinates2, ["2.500", "5.000", "10.000", "25.000", "50.000", "100.000", "250.000", "500.000", "750.000", "1.000.000"])]

        self.suitcases = [Suitcase(x, y, suitcase_IMG, 1, i + 1, self.prizes[i]) for i, (x, y) in enumerate(self.coordinates)]

    def display_popup(self, prize, suitcase_number):
        popup_width, popup_height = goldButton_IMG.get_size()
        popup_x = (self.YUKSEKLIK - popup_width) // 2 - 100
        popup_y = (self.GENISLIK - popup_height) // 2 - 120
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
        
        popup_start_time = time.time()
        popup_display_duration = 4.5

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(goldButton_IMG, popup_rect.topleft)

            suitcase_text = FONT2.render(f"Suitcase {suitcase_number}", True, WESTERNCOLOR)
            prize_text = FONT4.render(f"Prize: ${prize}", True, NORMALINSAN_KONUSMA)

            suitcase_text_rect = suitcase_text.get_rect(center=(popup_x + popup_width // 2 + 60, popup_y + popup_height // 2 - 60))
            prize_text_rect = prize_text.get_rect(center=(popup_x + popup_width // 2 + 65, popup_y + popup_height // 2 + 10))

            self.screen.blit(suitcase_text, suitcase_text_rect)
            self.screen.blit(prize_text, prize_text_rect)
            self.screen.blit(presenter1_IMG, (750, 30))

            pygame.display.update()
            self.clock.tick(self.FPS)
            
            if time.time() - popup_start_time > popup_display_duration:
                break

    def reveal_matching_money_bar(self, prize):
        for money_bar in self.money_bars_left + self.money_bars_right:
            if money_bar.is_match(prize):
                money_bar.reveal()

    def play_clapping_sound(self, prize):
        low_prizes = {"1", "10", "25", "50", "75", "100", "250", "500", "750", "1.000"}

        if prize in low_prizes:
            normal_clapping_effect.play()
        else:
            lower_clapping_effect.play()

    def bankaci(self, offer):
        self.banker_offer = offer

        formatted_offer = format_number(offer)
        popup_width, popup_height = goldButton_IMG.get_size()
        popup_x = (self.YUKSEKLIK - popup_width) // 2 - 100
        popup_y = (self.GENISLIK - popup_height) // 2 - 40
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)

        offer_text = FONT3.render(f"My offer is ${formatted_offer}", True, DARK_COFFEE)
        offer_text_rect = offer_text.get_rect(center=(popup_x + popup_width // 2 + 50, popup_y + popup_height // 2 - 40))

        decision_made = False

        while not decision_made:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(goldButton_IMG, popup_rect.topleft)
            self.screen.blit(offer_text, offer_text_rect)
            draw_text("Either accept the offer and leave, or keep playing!", FONT1, BLACK, 90, 140)
            
            tick_button_clicked = tick_button.draw(self.screen)
            cross_button_clicked = cross_button.draw(self.screen)

            self.screen.blit(banker_IMG, (750, 105))

            pygame.display.update()
            self.clock.tick(self.FPS)

            if tick_button_clicked:
                decision_made = True
                return True
            elif cross_button_clicked:
                decision_made = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        time.sleep(0.8)
        return False

    def game_ending_by_banker(self):
        start_time2 = time.time()
        while True:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(dialogue_IMG, (90, 100))
            draw_text("You accepted the banker's offer!", FONT1, BLACK, 190, 180)
            draw_text("You won", FONT3, BLACK, 330, 210)
            self.screen.blit(dollar_IMG, (230, 270))
            draw_text(f"${format_number(self.banker_offer)}", FONT4, DARK_GREEN, 310, 260)
            self.screen.blit(banker_IMG, (720, 105))

            pygame.display.update()
            self.clock.tick(self.FPS)

            if time.time() - start_time2 > 10:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        pygame.quit()
        exit()

    def normal_game_ending(self, suitcase_number, prize):
        start_time3 = time.time()
        run = True
        while run:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(dialogue_IMG, (70, 100))
            draw_text(f"You chose suitcase {suitcase_number}", FONT2, BLACK, 210, 160)
            draw_text("You won", FONT3, DARK_COFFEE, 310, 205)
            self.screen.blit(dollar_IMG, (190, 255))
            draw_text(f"${prize}", FONT4, DARK_GREEN, 270, 250)
            self.screen.blit(presenter3_IMG, (685, 110))

            if time.time() - start_time3 > 12:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.update()
            self.clock.tick(self.FPS)

        pygame.quit()
        exit()

    def run(self):
        pygame.display.set_caption("Prize or Surprise")
        speed_thrill_beat_music.play(-1)
        while True:
            current_time = time.time()

            if not self.popup_active and not self.delay_active:
                self.screen.blit(self.background, (0, 0))

                for suitcase in self.suitcases[:]:
                    if suitcase.draw(self.screen):
                        print(f"Suitcase number {suitcase.number} clicked! It contains: {suitcase.prize}")

                        if len(self.suitcases) == 2:
                            self.selected_suitcase = suitcase
                            other_suitcase = [s for s in self.suitcases if s != suitcase][0]

                            if int(suitcase.prize.replace('.', '')) > int(other_suitcase.prize.replace('.', '')):
                                cheering_and_clapping_effect.play()
                            else:
                                lower_cheering_and_clapping_effect.play()

                        else:
                            self.play_clapping_sound(suitcase.prize)

                        self.popup_active = True
                        self.popup_end_time = current_time + 1
                        self.display_popup(suitcase.prize, suitcase.number)
                        self.reveal_matching_money_bar(suitcase.prize)
                        self.suitcases.remove(suitcase)
                        self.suitcases_opened += 1

                        if self.suitcases_opened == 6 or (self.suitcases_opened > 6 and (self.suitcases_opened - 6) % 3 == 0):
                            self.delay_active = True
                            self.delay_end_time = current_time + 8

                            remaining_prizes = [s.prize for s in self.suitcases]
                            average_prize = sum([int(p.replace('.', '')) for p in remaining_prizes]) // len(remaining_prizes)
                            self.banker_offer = round(average_prize // 2, -2)

                        break

                for money_bar in self.money_bars_left + self.money_bars_right:
                    money_bar.draw(self.screen)

                if len(self.suitcases) == 2:
                    draw_text("Choose a suitcase to keep it", FONT3, WHITE, 255, 550)
                    draw_text("for you!!", FONT2, WHITE, 450, 590)

                elif len(self.suitcases) == 1 and self.selected_suitcase:
                    self.normal_game_ending(self.selected_suitcase.number, self.selected_suitcase.prize)
                    break

            elif self.delay_active:
                self.screen.blit(self.background, (0, 0))
                for suitcase in self.suitcases:
                    suitcase.draw(self.screen)
                for money_bar in self.money_bars_left + self.money_bars_right:
                    money_bar.draw(self.screen)

                draw_text("Banker thinks...", FONT4, GREEN, 330, 550)

                pygame.display.update()
                self.clock.tick(self.FPS)

                if current_time > self.delay_end_time:
                    self.delay_active = False
                    if self.bankaci(self.banker_offer):
                        cheering_and_clapping_effect.play()
                        self.game_ending_by_banker()
                        break

            else:
                if current_time > self.popup_end_time:
                    self.popup_active = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(self.FPS)

        pygame.quit()
        exit()