"""
This is our main driver file. It will be reponsible for handling user input, game state obj and displaying the game.
"""
import pygame as p
from settings import *
from spritesheet import *
from editorEngine import *
import json
from mainGame import draw_text, get_text_as_img
from button import *

original_image = p.transform.scale(p.image.load("images/Pics.png"), (512, 512) )



image = SpriteSheet(original_image)
def loadImages():
    scale = 16
    for y in range(32):
        for x in range(32):
            IMAGES[f"{x}, {y}"] =  image.get_image(1, x*scale, y*scale, scale, scale, SQ_SIZE, SQ_SIZE)
    #Note: we can acces an image by saying image["lname"]

# global variables
sq_selected = () #no square is selected, keep track of last click of the user (tuple; (row, col))


def main():
    p.init()
    font = p.font.SysFont("Helvetica", 16, True, False) #12 size original 16 good
    font_big = p.font.SysFont("Helvetica", 32, True, False) #12 size original 16 good

    screen = p.display.set_mode((BOARD_WIDTH + EDIT_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()

    moveLogFont = p.font.SysFont("Arial", 16, False, False) #12 size original 16 good


    loadImages() #loading in images

    p.display.set_icon(IMAGES["1, 1"]) #ICON
    p.display.set_caption("Chess") #TITLE of game

    #settings and game engine
    settings = Settings()
    gs = GameState()



    


    while settings.running:
        
        if settings.state == 0: # normal
            screen.fill((79, 161, 101), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
            event_handler(settings, gs)
            draw(screen, gs, font, settings.is_edit_upper)
        if settings.state == 4: # map
            screen.fill((0, 0, 100), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
            event_handler_map(settings, gs) # må endres senere!!
            draw_map(screen, gs, font_big, settings)
            map_menu(screen, font, gs, settings)

        clock.tick(MAX_FPS)
        p.display.flip()  

def event_handler(settings, gs):
    # global sq_selected
    # global is_edit_upper

    for e in p.event.get():
            if e.type == p.QUIT:
                settings.running = False
            
            #mouseclicks
            elif e.type == p.MOUSEBUTTONDOWN:
                within_board = True
                location = p.mouse.get_pos() #(x, y ) loc of mouse
                col, row = location

                if col > BOARD_WIDTH: #clicked outside board
                    within_board = False
                    row = row // 16
                    col = (col - BOARD_WIDTH) // 16
                    settings.sq_selected = (col, row)
                    
                else: #clicked inside
                    row = row // SQ_SIZE
                    col = col // SQ_SIZE
                    if settings.sq_selected != ():
                            if settings.is_edit_upper:
                                if settings.sq_selected != (0, 0):
                                    gs.board_upper[col][row] = f"{settings.sq_selected[0]}, {settings.sq_selected[1]}"
                                else:
                                    gs.board_upper[col][row] = "--"

                            else:
                                if settings.sq_selected != (0, 0):
                                    gs.board_under[col][row] = f"{settings.sq_selected[0]}, {settings.sq_selected[1]}"
                                else:
                                    gs.board_under[col][row] = "--"




            #keyboardpresses
            elif e.type == p.KEYDOWN:
                if e.key == p.K_1:
                    settings.is_edit_upper = False
                elif e.key == p.K_2:
                    settings.is_edit_upper = True
                elif e.key == p.K_s:
                    inp = input("are you sure?  y/n-->")
                    if inp.lower() == "y":
                        gs.map_dict[gs.curr_level][gs.curr_map]["upper"] = gs.board_upper
                        gs.map_dict[gs.curr_level][gs.curr_map]["under"] = gs.board_under
                        with open(f"data/maps/test.json", "w") as outfile:
                            json.dump(gs.map_dict, outfile)
                        print(f"saved map to level: {gs.curr_level}, map: {gs.curr_map}")

                elif e.key == p.K_TAB:
                    settings.state = 4 if settings.state == 0 else 0

def event_handler_map(settings, gs):
    # global sq_selected
    # global is_edit_upper

    for e in p.event.get():
            if e.type == p.QUIT:
                settings.running = False
            
            #mouseclicks
            # elif e.type == p.MOUSEBUTTONDOWN:
            #    pass

            #keyboardpresses
            elif e.type == p.KEYDOWN:

                if e.key == p.K_TAB:
                    settings.state = 4 if settings.state == 0 else 0
          



def draw(screen, gs, font, edit):
    draw_background(screen, gs)
    draw_edit_photo(screen)
    draw_editing(screen, font, edit)



def draw_background(screen, gs):
    for y in range(DIMENSION):
        for x in range(DIMENSION):
            if gs.board_under[x][y] != "--":
                screen.blit(IMAGES[gs.board_under[x][y]], (x*SQ_SIZE, y*SQ_SIZE))
            if gs.board_upper[x][y] != "--":
                screen.blit(IMAGES[gs.board_upper[x][y]], (x*SQ_SIZE, y*SQ_SIZE))


def draw_edit_photo(screen):
    screen.blit(original_image, (BOARD_WIDTH, 0))

def draw_editing(screen, font, edit):
    text = "upper" if edit else "under"
    x, y = BOARD_WIDTH + EDIT_PANEL_WIDTH - 100, BOARD_HEIGHT-100
    p.draw.rect(screen, "black", (x-20, y-20, 40, 40))
    draw_text(screen, text, font, x, y)

def draw_map(screen, gs, font, settings):
    liste = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    width = 50
    x, y = BOARD_WIDTH // 2 -width//2, BOARD_WIDTH // 2 -width//2
    # p.draw.rect(screen, "black", (x, y, width, width)) 
    for map in gs.map_dict[gs.curr_level]:
        map_x = int(map[0])
        map_y = int(map[-1])
        color = "red" if map == gs.curr_map else "black"
        draw_rect_with_borders(screen, color, "white", x+map_x*width, y-map_y*width, width, width)

        # add pluss button
        for thing in liste:
            meta_x, meta_y = map.strip().split(", ")
            meta_x, meta_y = int(meta_x), int(meta_y)
            meta_x = meta_x + thing[0]
            meta_y = meta_y + thing[1]
            string = f"{meta_x}, {meta_y}"
            if string not in gs.map_dict[gs.curr_level]:
                img = get_text_as_img("+", font)
                if Button(screen, x + width*meta_x, y - width*meta_y, img, width, width).draw(settings):
                    print(f"{string}")

def draw_rect_with_borders(screen, color, color_border, x, y, width, height):
    p.draw.rect(screen, color, (x,y,width,height), 0)
    for i in range(4):
        p.draw.rect(screen, color_border, (x-i,y-i,width,height), 1)

def map_menu(screen, font, gs, settings):
    button_pressed = False
    new_level = None
    new_map = None
    y = 0
    x = 50
    height = 20
    draw_text(screen, "LEVELS", font, x, y)
    y += height
    for level in gs.map_dict:
        img = get_text_as_img(level, font)
        if Button(screen, x, y, img, img.get_width(), img.get_height()).draw(settings):
            print(level)
            button_pressed = True
            new_level = level
        y += height
    y += height

    draw_text(screen, "MAPS", font, x, y)
    y += height
    for map in gs.map_dict[gs.curr_level]:
        img = get_text_as_img(map, font)
        if Button(screen, x, y, img, img.get_width(), img.get_height()).draw(settings):
            print(map)
            button_pressed = True
            new_map = map
        y += height
    y += height

    if button_pressed:
        if new_level:
            gs.load_current_map(new_level, "0, 0")
            gs.curr_level = new_level

        elif new_map:
            gs.load_current_map(gs.curr_level, new_map)
            gs.curr_map = new_map



if __name__ == "__main__":
    main()