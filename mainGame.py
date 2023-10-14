"""
This is our main driver file. It will be reponsible for handling user input, game state obj and displaying the game.
"""

from settings import *
from spritesheet import *
from engine import *
from button import *
import json
import math
import random

original_image = p.transform.scale(p.image.load("images/Pics.png"), (512, 512) )
image = SpriteSheet(original_image)
scale = 16

#all images as squares
def loadImages():
    for y in range(32):
        for x in range(32):
            IMAGES[f"{x}, {y}"] =  image.get_image(1, x*scale, y*scale, scale, scale, SQ_SIZE, SQ_SIZE)
    #Note: we can acces an image by saying image["lname"]

def load_sprite_images(num_frames=[4, 5], start_loc=[(8, 4), (8+3, 4)], width=2, height=1):
    ret_list = []
    for times in range(len(num_frames)):
        temp_list = []
        for i in range(num_frames[times]):
            temp_list.append(image.get_image(1, (start_loc[times][0]*scale + i*scale), start_loc[times][1]*scale, height*scale, width*scale, SQ_SIZE*height, SQ_SIZE*width))
        ret_list.append(temp_list)
    return ret_list




# global variables
# sq_selected = () #no square is selected, keep track of last click of the user (tuple; (row, col))
# is_edit_upper = True

# loadImages() #loading in images
# animations = {}
# animations["knight"] = load_sprite_images()
# animations["witch"] = load_sprite_images([4], [(23, 17)], width=1, height=1)
# animations["mage"] = load_sprite_images([4, 5], [(8, 8), (11, 8)])
# animations["mage2"] = load_sprite_images([4, 5], [(8, 10), (11, 10)])
# animations["indicator"] = load_sprite_images([1], [(19, 11)])[0]


# #settings and game engine
# settings = Settings()
# gs = GameState(animations)
def main():
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MENU_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()


    font_big = p.font.SysFont("Helvetica", 32, True, False) #12 size original 16 good
    font = p.font.SysFont("Helvetica", 16, True, False) #12 size original 16 good

    loadImages() #loading in images
    animations = {}
    animations["knight"] = load_sprite_images()
    animations["witch"] = load_sprite_images([4], [(23, 17)], width=1, height=1)
    animations["mage"] = load_sprite_images([4, 5], [(8, 8), (11, 8)])
    animations["mage2"] = load_sprite_images([4, 5], [(8, 10), (11, 10)])
    animations["indicator"] = load_sprite_images([1], [(19, 11)])[0]

    p.display.set_icon(IMAGES["1, 1"]) #ICON
    p.display.set_caption("RPG STUFF") #TITLE of game

    #settings and game engine
    settings = Settings()
    gs = GameState(animations)



    


    while settings.running:
        
        screen.fill((0, 0, 20), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
        screen.fill((0, 0, 20), (BOARD_WIDTH, 0, MENU_PANEL_WIDTH, BOARD_HEIGHT))

        draw_menu_border(screen, gs)

        if settings.state == 0: #normal
            event_handler_normal(settings, gs, screen)
            draw_normal(screen, gs, settings, font)
            update_normal(gs, settings)
        elif settings.state == 1: # combat
            event_handler_combat(settings, gs)
            draw_combat(screen, gs, font, font_big, settings)
            update_combat(screen, gs, font, settings)
        elif settings.state == 2: #lost
            event_handler_lost(settings, gs)
            draw_lost(screen, gs, settings, font_big)
            if update_lost(screen, font_big, settings):
                settings = Settings()
                gs = GameState(animations)
        elif settings.state == 3: #victory combate screen
            event_handler_vic(settings, gs)
            draw_vic(screen, gs, settings, font_big, font)
            if update_vic(screen, font, settings, gs):
                settings.state = 0
        elif settings.state == 4: # map
            screen.fill((0, 0, 100), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
            event_handler_map(settings, gs) # må endres senere!!
            draw_map(screen, gs)


        clock.tick(MAX_FPS)
        p.display.flip()  


###### normal event handler ###########
def event_handler_normal(settings, gs, screen):
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

                if col > BOARD_WIDTH: #clicked on menu
                    within_board = False
                    row = row // 16
                    col = (col - BOARD_WIDTH) // 16
                    gs.sq_selected = (col, row)
                    
                else: #clicked inside
                    row = row // SQ_SIZE
                    col = col // SQ_SIZE
                    gs.hero.goal_x = col*SQ_SIZE
                    gs.hero.goal_y = row*SQ_SIZE - gs.hero.animation_list[0][0].get_height() // 2



            #keyboardpresses
            elif e.type == p.KEYDOWN:
                if e.key == p.K_1:
                    gs.current_heroes[0].action += 1
                    gs.current_heroes[0].frame_index = 0
                    if gs.current_heroes[0].action >= len(gs.current_heroes[0].animation_list):
                        gs.current_heroes[0].action = 0
                        

                elif e.key == p.K_2:
                    pass

                elif e.key == p.K_s:
                    # inp = input("name of file")
                    inp = "start"
                    dic = {
                        "under": gs.board_under, 
                        "upper": gs.board_upper,
                        "heroes": gs.current_heroes,
                        "enemies": gs.current_enemies
                        }
                    with open(f"data/maps/{inp}.json", "w") as outfile:
                        json.dump(dic, outfile)
                elif e.key == p.K_i: #toggle fullscreen
                    if not settings.fullscreen:
                        screen = p.display.set_mode((BOARD_WIDTH + MENU_PANEL_WIDTH, BOARD_HEIGHT), pygame.FULLSCREEN)
                        settings.fullscreen = True
                    else:
                        screen = p.display.set_mode((BOARD_WIDTH + MENU_PANEL_WIDTH, BOARD_HEIGHT))
                        settings.fullscreen = False
                elif e.key == p.K_TAB:
                    settings.state = 4 if settings.state == 0 else 0
          



                
########## Drawing normal ###############

def draw_normal(screen, gs, settings, font):
    draw_background_under(screen, gs)
    draw_current_hero(screen, gs)
    draw_current_enemies(screen, gs, settings)
    draw_background_upper(screen, gs)
    draw_gold_and_xp(screen, gs, font)

def draw_background_under(screen, gs):
    for y in range(DIMENSION):
        for x in range(DIMENSION):
            if gs.board_under[x][y] != "--":
                screen.blit(IMAGES[gs.board_under[x][y]], (x*SQ_SIZE, y*SQ_SIZE))


def draw_background_upper(screen, gs):
    for y in range(DIMENSION):
        for x in range(DIMENSION):
            if gs.board_upper[x][y] != "--":
                screen.blit(IMAGES[gs.board_upper[x][y]], (x*SQ_SIZE, y*SQ_SIZE))


def draw_current_hero(screen, gs):
    hero = gs.hero
    screen.blit(hero.animation_list[hero.action][hero.frame_index], (hero.x, hero.y))
    
    if p.time.get_ticks() - hero.update_time > hero.animation_cooldown:
        hero.update_time = p.time.get_ticks()
        hero.frame_index += 1
        if hero.frame_index >= len(hero.animation_list[hero.action]):
            hero.frame_index = 0

    if hero.x != hero.goal_x or hero.y != hero.goal_y: #move to wanted location
        hero.run()
        dx = hero.goal_x - hero.x
        dy = hero.goal_y - hero.y
        if dx != 0:
            hero.x += math.floor((dx)/abs(dx))*hero.speed
        if dy != 0:
            hero.y += math.floor((dy)/abs(dy)*hero.speed)
    else:
        hero.idle()

def draw_current_hero_and_allies(screen, gs):
    for hero in gs.hero.crew:
        screen.blit(hero.animation_list[hero.action][hero.frame_index], (hero.x, hero.y))
        
        if p.time.get_ticks() - hero.update_time > hero.animation_cooldown:
            hero.update_time = p.time.get_ticks()
            hero.frame_index += 1
            if hero.frame_index >= len(hero.animation_list[hero.action]):
                hero.frame_index = 0

        if hero.x != hero.goal_x or hero.y != hero.goal_y: #move to wanted location
            hero.run()
            dx = hero.goal_x - hero.x
            dy = hero.goal_y - hero.y
            move_amount = [0, 0]
            if dx != 0:
                move_amount[0] = math.floor((dx)/abs(dx)*hero.speed)
                hero.x += move_amount[0]
            if dy != 0:
                move_amount[1] = math.floor((dy)/abs(dy)*hero.speed)
                hero.y += move_amount[1]
            if abs(dx) < SQ_SIZE:
                hero.x = hero.goal_x
            if abs(dy) < SQ_SIZE:
                hero.y = hero.goal_y
        else:
            hero.idle()
        hero.rect.x = hero.x
        hero.rect.y = hero.y


def draw_current_enemies(screen, gs, settings):
    enemy_list = gs.combat.main_enemy.crew if settings.state == 1 else gs.current_enemies #changes list to crew if in combat
    for enemy in enemy_list:
        if type(enemy) == list: #for the nested list of current enemies get the first one in a list
            enemy = enemy[0]
        screen.blit(enemy.animation_list[enemy.action][enemy.frame_index], (enemy.x, enemy.y))
        
        if p.time.get_ticks() - enemy.update_time > enemy.animation_cooldown:
            enemy.update_time = p.time.get_ticks()
            enemy.frame_index += 1
            if enemy.frame_index >= len(enemy.animation_list[enemy.action]):
                enemy.frame_index = 0

        if enemy.x != enemy.goal_x or enemy.y != enemy.goal_y: #move to wanted location
            dx = enemy.goal_x - enemy.x
            dy = enemy.goal_y - enemy.y
            if dx != 0:
                enemy.x += math.floor((dx)/abs(dx)*enemy.speed)
            if dy != 0:
                enemy.y += math.floor((dy)/abs(dy)*enemy.speed)
            if abs(dx) < SQ_SIZE:
                enemy.x = enemy.goal_x
            if abs(dy) < SQ_SIZE:
                enemy.y = enemy.goal_y

def draw_gold_and_xp(screen, gs, font):
    draw_text(screen, f"Gold: {gs.current_player_gold}", font, 
        BOARD_WIDTH + MENU_PANEL_WIDTH//2,
        (SQ_SIZE*DIMENSION-SQ_SIZE*2)+SQ_SIZE//2*0)
    draw_text(screen, f"XP: {gs.current_player_xp}", font, 
        BOARD_WIDTH + MENU_PANEL_WIDTH//2,
        (SQ_SIZE*DIMENSION-SQ_SIZE*2)+SQ_SIZE//2*1)


def update_normal(gs, settings):
    for enemy in gs.current_enemies:
        enemy = enemy[0]
        if enemy.x == gs.hero.x and enemy.y+SQ_SIZE*(enemy.height-1)  == gs.hero.y+SQ_SIZE*(gs.hero.height-1): #+SQ_SIZE e ein quickfix #transition to combat
            settings.state = 1 #initiate combat
            gs.combat = Combat(gs.hero.crew, enemy.crew, gs)

            for i, hero in enumerate(gs.hero.crew):
                if not hero.in_combat:
                    hero.pos_before_fight = [hero.goal_x, hero.goal_y]
                    hero.in_combat = True
                hero.goal_x = 2*SQ_SIZE
                hero.goal_y = BOARD_HEIGHT//len(gs.hero.crew) * (i)
            for i, enemy in enumerate(enemy.crew):
                if not enemy.in_combat:
                    enemy.pos_before_fight = [enemy.x, enemy.y]
                    enemy.in_combat = True
                enemy.goal_x = 13*SQ_SIZE
                enemy.goal_y = BOARD_HEIGHT//len(enemy.crew) * (i) + SQ_SIZE - (SQ_SIZE*(enemy.height -1))
                # enemy.goal_y = BOARD_HEIGHT//len(enemy.crew) * (i) + SQ_SIZE
    gs.change_map()



##################################################################################

################ COMBAT ##########################################################
def event_handler_combat(settings, gs):
    for e in p.event.get():
            if e.type == p.QUIT:
                settings.running = False
            
            #mouseclicks
            elif e.type == p.MOUSEBUTTONDOWN:
                within_board = True
                location = p.mouse.get_pos() #(x, y ) loc of mouse
                col, row = location

                if col > BOARD_WIDTH: #clicked on menu
                    within_board = False
                    row = row // 16
                    col = (col - BOARD_WIDTH) // 16
                    gs.sq_selected = (col, row)
                    
                else: #clicked inside
                    row = row // SQ_SIZE
                    col = col // SQ_SIZE
                    gs.combat.change_target(gs, location) #changes the target if you click on them
                                


            #keyboardpresses
            elif e.type == p.KEYDOWN:
                if e.key == p.K_1:
                    pass
                elif e.key == p.K_2:
                    pass


def draw_combat(screen, gs, font, font_big, settings):
    draw_current_hero_and_allies(screen, gs)
    draw_current_enemies(screen, gs, settings)
    draw_turn_indicator(screen, gs, settings)
    draw_target_indicator(screen, gs, settings)
    draw_combat_doing(screen, gs, settings, font)
    draw_health(screen, gs, settings, font)
    draw_text(screen, "BATTLE!", font_big, BOARD_WIDTH + MENU_PANEL_WIDTH//2, SQ_SIZE//2) #battle title

    gs.damage_text_group.draw(screen)
    # draw_turn_indicator_test(screen, gs)

def draw_turn_indicator(screen, gs, settings):
    combat = gs.combat
    if combat.turn_index >= len(combat.allies_and_enemies):
        combat.turn_index -= 1
    
    combatant = combat.allies_and_enemies[combat.turn_index]
    coords = (
        combatant.x, 
        combatant.y + (SQ_SIZE * (combatant.height))
        )
    if p.time.get_ticks() - settings.indicator_time > settings.indicator_cooldown:
        settings.arrow_show = not settings.arrow_show
        settings.indicator_time = p.time.get_ticks()
    if settings.arrow_show:
        screen.blit(gs.indicator[0], coords)

def draw_target_indicator(screen, gs, settings):
    combat = gs.combat
    combatant = combat.target
    coords = (
        combatant.x, 
        combatant.y
        )
    if p.time.get_ticks() - settings.target_time > settings.target_cooldown:
        settings.target_show = not settings.target_show
        settings.target_time = p.time.get_ticks()
    if settings.target_show:
        height, width = combatant.animation_list[0][0].get_height(), combatant.animation_list[0][0].get_width() 
        screen.blit(combatant.mask_image, coords)

def draw_combat_doing(screen, gs, settings, font):
    if settings.display_text:
        texts = [settings.text, settings.text_2, settings.text_3]
        for i, text in enumerate(texts):
            draw_text(screen, text, font, 
                BOARD_WIDTH + MENU_PANEL_WIDTH//2,
                (SQ_SIZE*DIMENSION-SQ_SIZE*2)+SQ_SIZE//2*i)
            
    if p.time.get_ticks() - settings.text_start_time > settings.text_time:
        settings.display_text = False


def draw_health(screen, gs, settings, font):
    for figther in gs.combat.allies_and_enemies:
        text = f"{figther.hp}/{figther.max_hp}"
        draw_text(screen, text, font, 
                  figther.x + SQ_SIZE//2, 
                  figther.y + SQ_SIZE*(figther.height-1) + SQ_SIZE)
    


def update_combat(screen, gs, font, settings):
    gs.damage_text_group.update()
    combatant = gs.combat.allies_and_enemies[gs.combat.turn_index]
    target = gs.combat.target
    move_made = None
    text = ""
    for text in gs.damage_text_group:
        if p.time.get_ticks() - text.created > settings.text_ttl:
            text.kill()

    if gs.combat.ally_turn: #ally turn
        # combat moves and buttons etc
        button_pressed = None
        for i, combat_move in enumerate(combatant.combat_moves_list):
            img = get_text_as_img(f"{i+1}. " +combat_move.name, font)
            button = Button(screen, BOARD_WIDTH + MENU_PANEL_WIDTH//2 -img.get_width()//2 - SQ_SIZE*2 ,SQ_SIZE + SQ_SIZE//2*(i+1), img, img.get_width(), img.get_height())
            if button.draw(settings): #button pressed
                button_pressed = combat_move.name
                move_made = combat_move

        
        if button_pressed == "Run":
            print(f"{combatant.name} ran away")
            settings.text = f"{combatant.name} ran away"
            gs.end_combat(settings) #currently just ends combat

        elif button_pressed == "Kick":
            print(f"{combatant.name} kicked {gs.combat.target.name}")
            settings.text = f"{combatant.name} kicked {gs.combat.target.name}"

        settings.enemy_wait_start_time =  p.time.get_ticks() #for å gjøre slik at den første holdes like lenge

    else: #enemy turn
        c = gs.combat
        c.target = random.choice(c.allies)
        if p.time.get_ticks() - settings.enemy_wait_start_time > settings.enemy_wait:
            move_made = c.turn.combat_moves_list[0]
            settings.text = f"{combatant.name} kicked {gs.combat.target.name}"

            settings.enemy_wait_start_time = p.time.get_ticks()

    if move_made is not None:
        if move_made.damage != 0:
            settings.text_2 = f"For {move_made.damage} damage"
        if move_made.heal != 0:
            settings.text_3 = f"Healing for {move_made.heal}"
        gs.combat.move_hp_and_write(move_made, font, gs)
        settings.text_start_time = p.time.get_ticks()
        settings.display_text = True
    
    #fighter update
    for i, fighter in enumerate(gs.combat.allies_and_enemies):
        fighter.update()
        if not fighter.alive:
            gs.combat.loot_xp_earned += fighter.loot_xp
            gs.combat.loot_gold_earned += fighter.loot_gold
            gs.combat.allies_and_enemies.pop(i)
            for i, figther_2 in enumerate(gs.combat.enemies):
                if figther_2 == fighter:
                    gs.combat.enemies.pop(i)
            for i, figther_2 in enumerate(gs.combat.allies):
                if figther_2 == fighter:
                    gs.combat.allies.pop(i)
            for i, fighter_2 in enumerate(fighter.crew):
                if fighter_2 == fighter:
                    fighter.crew.pop(i)
            for i, fighter_2 in enumerate(gs.current_enemies):
                if fighter_2 == fighter:
                    gs.current_enemies.pop(i)
            for i, fighter_2 in enumerate(gs.current_allies):
                if fighter_2 == fighter:
                    gs.current_allies.pop(i)
            if len(gs.combat.enemies) == 0:
                print("won")
                gs.end_combat(settings)
                settings.state = 3
            elif len(gs.combat.allies) == 0:
                gs.end_combat(settings)
                settings.state = 2
                print("lost")
            else:
                gs.combat.target = gs.combat.enemies[0] if gs.combat.ally_turn else gs.combat.allies[0] #må fikse en if statement her ens
            
            

##########################################################

############################# Lost #######################  
def draw_lost(screen, gs, settings, font_big):
    draw_text(screen, "You were defeated in the Dungeons", font_big, BOARD_WIDTH//2, BOARD_HEIGHT//2//2)
                
def event_handler_lost(settings, gs):
    for e in p.event.get():
            if e.type == p.QUIT:
                settings.running = False

def update_lost(screen, font, settings):
    lost_text = get_text_as_img("Try again?", font)
    width, height = lost_text.get_width(), lost_text.get_height()
    s = settings
    if Button(screen, BOARD_WIDTH//2 - width//2, BOARD_HEIGHT//2, lost_text, 
              width, height).draw(s):
        return True
    return False

##########################################################

##################### Combat Victory Screen ##############

def draw_vic(screen, gs, settings, font_big, font):
    draw_text(screen, "Battle Won!", font_big, BOARD_WIDTH//2, BOARD_HEIGHT//2//2)
    draw_text(screen, f"gold earned: {gs.combat.loot_gold_earned}", font, BOARD_WIDTH//2, BOARD_HEIGHT//2//1.55) #just for show atm
    draw_text(screen, f"XP earned: {gs.combat.loot_xp_earned}", font, BOARD_WIDTH//2, BOARD_HEIGHT//2//1.7) #just for show atm
                
def event_handler_vic(settings, gs):
    for e in p.event.get():
            if e.type == p.QUIT:
                settings.running = False

def update_vic(screen, font, settings, gs):
    vic_text = get_text_as_img("Continue", font)
    if not settings.combat_gotten_xp:
        gs.current_player_xp += gs.combat.loot_xp_earned
        gs.current_player_gold += gs.combat.loot_gold_earned
        settings.combat_gotten_xp = True
    width, height = vic_text.get_width(), vic_text.get_height()
    s = settings
    if Button(screen, BOARD_WIDTH//2 - width//2, BOARD_HEIGHT//2, vic_text, 
              width, height).draw(s):
        settings.combat_gotten_xp = False
        return True
    return False

##########################################################

##################### Map/TAB-menu #######################

def draw_map(screen, gs):
    width = 50
    x, y = BOARD_WIDTH // 2 -width//2, BOARD_WIDTH // 2 -width//2
    # p.draw.rect(screen, "black", (x, y, width, width)) 
    for map in gs.map_dict[gs.curr_level]:
        map_x = int(map[0])
        map_y = int(map[-1])
        color = "red" if map == gs.curr_map else "black"
        draw_rect_with_borders(screen, color, "white", x+map_x*width, y-map_y*width, width, width)

def draw_rect_with_borders(screen, color, color_border, x, y, width, height):
    p.draw.rect(screen, color, (x,y,width,height), 0)
    for i in range(4):
        p.draw.rect(screen, color_border, (x-i,y-i,width,height), 1)

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
          



##########################################################

##################### General ############################

def draw_menu_border(screen, gs):
    for i in range(BOARD_HEIGHT//SQ_SIZE):#left
        screen.blit(p.transform.rotate(IMAGES["0, 8"], 180), (BOARD_WIDTH, i*SQ_SIZE))
    for i in range(BOARD_HEIGHT//SQ_SIZE):#right
        screen.blit(IMAGES["0, 8"], (BOARD_WIDTH+MENU_PANEL_WIDTH-SQ_SIZE, i*SQ_SIZE))
    for i in range(MENU_SIZE):#upper
        screen.blit(p.transform.rotate(IMAGES["0, 8"], 90), (BOARD_WIDTH + i*SQ_SIZE, 0))
    for i in range(MENU_SIZE):#lower
        screen.blit(p.transform.rotate(IMAGES["0, 8"], 270), (BOARD_WIDTH + i*SQ_SIZE, BOARD_HEIGHT-SQ_SIZE))





#create function for drawing text
def draw_text(screen, text, font, x, y):
    color1 = (p.color.Color("crimson"))
    color2 = (p.color.Color("grey"))
    img = font.render(text, True, color1)
    screen.blit(img, (x-(img.get_width()/2), y))
    img = font.render(text, True, color2)
    screen.blit(img, (x-(img.get_width()/2)+1, y+1))

def get_text_as_img(text, font):
    color1 = (p.color.Color("crimson"))
    color2 = (p.color.Color("grey"))
    img = font.render(text, True, color2)
    return img


if __name__ == "__main__":
    main()