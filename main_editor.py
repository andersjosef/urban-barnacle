"""
This is our main driver file. It will be reponsible for handling user input, game state obj and displaying the game.
"""
import pygame as p
from settings import *
from spritesheet import *
from editorEngine import *
import json

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
is_edit_upper = True


def main():
    p.init()
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
        
        screen.fill((79, 161, 101), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))

        event_handler(settings, gs)

        draw(screen, gs)


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
                    # inp = input("name of file")
                    inp = "start"
                    dic = {"under": gs.board_under, "upper": gs.board_upper}
                    with open(f"data/maps/{inp}.json", "w") as outfile:
                        json.dump(dic, outfile)

                



def draw(screen, gs):
    draw_background(screen, gs)
    draw_edit_photo(screen)


def draw_background(screen, gs):
    for y in range(DIMENSION):
        for x in range(DIMENSION):
            if gs.board_under[x][y] != "--":
                screen.blit(IMAGES[gs.board_under[x][y]], (x*SQ_SIZE, y*SQ_SIZE))
            if gs.board_upper[x][y] != "--":
                screen.blit(IMAGES[gs.board_upper[x][y]], (x*SQ_SIZE, y*SQ_SIZE))


def draw_edit_photo(screen):
    screen.blit(original_image, (BOARD_WIDTH, 0))

if __name__ == "__main__":
    main()