import pygame as p

#constants
BOARD_WIDTH = BOARD_HEIGHT = 800 #or 400
EDIT_PANEL_WIDTH = 512
MENU_PANEL_WIDTH = 300
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT

DIMENSION = 16
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MENU_SIZE = MENU_PANEL_WIDTH // SQ_SIZE
MAX_FPS = 60 # for animations
IMAGES = {}

BLUE = (80,100,175) # blue
WHITE = (255, 255, 255)
COLORS = [WHITE, BLUE]


class Settings:
    def __init__(self):
        self.running = True
        self.sq_selected = () #no square is selected, keep track of last click of the user (tuple; (row, col))
        self.is_edit_upper = True
        self.state = 0 #0: normal, 1:combat, 2: lost


        self.action = False
        self.clicked = False

        self.indicator_cooldown = 350
        self.indicator_time = p.time.get_ticks()
        self.arrow_show = True

        self.target_cooldown = 400
        self.target_time = p.time.get_ticks()
        self.target_show = True

        self.text_ttl = 1000

        self.enemy_wait_start_time = p.time.get_ticks()
        self.enemy_wait = 2500


        self.text_start_time = p.time.get_ticks()
        self.text_time = 2500
        self.display_text = False
        self.text = ""
        self.text_2 = ""
        self.text_3 = ""