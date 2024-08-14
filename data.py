import pygame
import buttons

pygame.init()

# height, width
YUKSEKLIK, GENISLIK = 1024, 636
FPS = 40
screen = pygame.display.set_mode((YUKSEKLIK, GENISLIK))
# pygame.display.set_caption("Prize or Surprise - Main Menu")
clock = pygame.time.Clock()

# fonts
FONT1 = pygame.font.Font("data/pixel-font.ttf", 25)
FONT2 = pygame.font.Font("data/pixel-font.ttf", 30)
FONT3 = pygame.font.Font("data/pixel-font.ttf", 35)
FONT4 = pygame.font.Font("data/pixel-font.ttf", 45)

def draw_text(text, font, text_col, x, y):
    msg = font.render(text, True, text_col)
    screen.blit(msg, (x, y))

def format_number(number):
    return f"{number:,}".replace(",", ".")

#background pictures
background1 = pygame.image.load("images/background/pixelart-nightpurple_bg.png")
background2 = pygame.image.load("images/background/pixelart-space_bg.png")
background3 = pygame.image.load("images/background/pixelart-orange_bg.png")
background4 = pygame.image.load("images/background/pixelart-train_bg.png")
start_background_bg = pygame.image.load("images/background/start-screen_bg.png")
main_menu1_bg = pygame.image.load("images/background/main_menu1_bg.png")
main_menu2_bg = pygame.image.load("images/background/main_menu2_bg.png")

# character pictures
banker_IMG = pygame.image.load("images/characters/banker_img.png")
presenter1_IMG = pygame.image.load("images/characters/presenter1_img.png")
presenter2_IMG = pygame.image.load("images/characters/presenter2_img.png")
presenter3_IMG = pygame.image.load("images/characters/presenter3_img.png")

# objects //pictures
dollar_IMG = pygame.image.load("images/objects/dollar_img.png")
gold_bar_IMG = pygame.image.load("images/objects/gold-bar_img.png")
goldButton_IMG = pygame.image.load("images/objects/goldButton_img.png")
suitcase_IMG = pygame.image.load("images/objects/suitcase_img.png")
dialogue_IMG = pygame.image.load("images/objects/dialogue_img.png")

# button pictures
start_img = pygame.image.load("images/buttons/start_button.png").convert_alpha()
quit_img = pygame.image.load("images/buttons/quit_button.png").convert_alpha()
resume_img = pygame.image.load("images/buttons/resume_button.png").convert_alpha()
options_img = pygame.image.load("images/buttons/options_button.png").convert_alpha()
settings_img = pygame.image.load("images/buttons/settings_button.png").convert_alpha()
controls_img = pygame.image.load("images/buttons/controls_button.png").convert_alpha()
back_img = pygame.image.load("images/buttons/back_button.png").convert_alpha()
home_img = pygame.image.load("images/buttons/home_button.png").convert_alpha()
left_button_img = pygame.image.load("images/buttons/left_button.png").convert_alpha()
right_button_img = pygame.image.load("images/buttons/right_button.png").convert_alpha()
tick_button_img = pygame.image.load("images/buttons/tick_button_img.png").convert_alpha()
cross_button_img = pygame.image.load("images/buttons/cross_button_img.png").convert_alpha()

# buttons
start_button = buttons.ButtonSoundedVersion(98, 475, start_img, 1)
quit_button = buttons.ButtonSoundedVersion(610, 475, quit_img, 1)
resume_button = buttons.ButtonSoundedVersion(354, 190, resume_img, 1)
options_button = buttons.ButtonSoundedVersion(354, 380, options_img, 1)
settings_button = buttons.ButtonSoundedVersion(98, 245, settings_img, 1)
controls_button = buttons.ButtonSoundedVersion(610, 245, controls_img, 1)
back_button = buttons.ButtonSoundedVersion(354, 410, back_img, 1)
home_button = buttons.ButtonSoundedVersion(15, 15, home_img, 0.75)
left_button = buttons.ButtonSoundedVersion(597.5, 185, left_button_img, 0.8)
right_button = buttons.ButtonSoundedVersion(717.5, 185, right_button_img, 0.8)

tick_button = buttons.ButtonSoundedVersion(378, 280, tick_button_img, 5)
cross_button = buttons.ButtonSoundedVersion(498, 280, cross_button_img, 5)

# music / sound effects
action_thrilling_music = pygame.mixer.Sound("music/action-thrilling_music.mp3")
action_thrilling_music.set_volume(0.25)

speed_thrill_beat_music = pygame.mixer.Sound("music/speed-thrill-beat_music.mp3")
speed_thrill_beat_music.set_volume(0.1)

lower_clapping_effect = pygame.mixer.Sound("music/lower_clapping_effect.mp3")
lower_clapping_effect.set_volume(1)

normal_clapping_effect = pygame.mixer.Sound("music/normal-clapping_effect.mp3")
normal_clapping_effect.set_volume(1)

cheering_and_clapping_effect = pygame.mixer.Sound("music/cheering-and-clapping_effect.mp3")
cheering_and_clapping_effect.set_volume(0.5)

lower_cheering_and_clapping_effect = pygame.mixer.Sound("music/small-applause_effect.mp3")
lower_cheering_and_clapping_effect.set_volume(0.25)

start_music = pygame.mixer.Sound("music/start_music.mp3")
start_music.set_volume(1)

start_effect = pygame.mixer.Sound("music/start_effect.mp3")
start_effect.set_volume(0.8)

exit_effect = pygame.mixer.Sound("music/exit_voice.mp3")
exit_effect.set_volume(1)

game_started_effect = pygame.mixer.Sound("music/coin-pickup_effect.mp3")
game_started_effect.set_volume(0.8)

winning_effect = pygame.mixer.Sound("music/winning_effect.mp3")
winning_effect.set_volume(0.4)

#colors
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
CHERRY = (210, 4, 45)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (250,250,250)
GRAY = (200,200,200)
AQUA = (0,255,255)
CHERRY = (210, 4, 45)
SEA_WHITE = (230, 255, 250)
DARK_WHITE = (210,211,232)
CADETBLUE = (152,245,255)
DARK_ORANGE = (255,97,3)
DARK_GREEN = (0,100,0)
DARK_PURPLE = (191,62,255)
DARK_COFFEE = (26,26,26)
SEE_BLUE = (30,144,255)
TURQOISE = (0,134,139)
WESTERNCOLOR = (58, 22, 14)
WESTERN_GREEN = (0,100,0)
WESTERN_BLUE= (20,26,135)
WESTERN_PINK = (186,84,98)
TEXT_DIS_ADAM_KONUSMA = (139,69,19)
NORMALINSAN_KONUSMA = (86,44,98)