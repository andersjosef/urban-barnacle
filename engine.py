from settings import *
from spritesheet import *
import json
import random


class GameState():
    def __init__(self, animations):

        ############################# BOARD and misc ####################################################

        # self.board_under = [["1, 4" for x in range(DIMENSION)] for x in range(DIMENSION)]
        # self.board_upper = [["--" for x in range(DIMENSION)] for x in range(DIMENSION)]
        self.curr_map = "start"
        self.load_current_map()
        self.animations = animations
        self.indicator = self.animations["indicator"]


        ############################# SPRITES ADDED IN GAME#####################################
        self.figures = {
                   "witch2": (7, 7, "Witch II", 100, 100, 1, 1,self.animations["witch"][:], 1, [], False, 5, 160),
                   "witch3": (7, 7, "Witch III", 100, 100, 1, 1,self.animations["witch"], 1, [], False, 5, 160),
                   "mage": (0, 2, "Mage", 100, 100, 1, 1, self.animations["mage"], 2, [], False, 10, 130),
                   "mage2": (0, 2, "Mage II", 100, 100, 1, 1, self.animations["mage2"], 2, [], False, 10, 130)
                   }
        self.figures["knight"] = (0, 2, "Knight", 100, 100, 1, 1, self.animations["knight"][:], 2, [], False, 10, 130)
        self.figures["witch"] =  (7, 7, "Witch", 100, 100, 1, 1,self.animations["witch"], 1, [], False, 5, 160)


        self.current_allies = self.create_ally_group(["knight", "mage"], 1, 1)
        self.hero = self.current_allies[0]

        self.current_enemies = []
        self.create_enemy_group(["mage", "witch"], 7, 7)



        #################### if in combat it will be a class ###################################
        self.enemy_in_combat_index = 0
        self.combat = None

        ####################Damage Text Group###################################################
        self.damage_text_group = pygame.sprite.Group()


    def load_current_map(self):
        with open(f"data/maps/{self.curr_map}.json", "r") as infile:
            dic =json.load(infile)
            self.board_under = dic["under"]
            self.board_upper = dic["upper"]

    def create_figther(self, name,x, y):
        info = self.figures[name]
        return Figure(x, y, info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10], info[11], info[12])

    def end_combat(self, settings):
        settings.state = 0
        for fighter in self.combat.allies_and_enemies:
            fighter.in_combat = False
            x, y = fighter.pos_before_fight

            # set their destination back to where they came form and move enemy so to not engage combat again
            if fighter in self.combat.enemies:
                fighter.goal_x = x + SQ_SIZE
            else:
                fighter.goal_x = x
            fighter.goal_y = y
        self.hero =self.current_allies[0]
        self.current_enemies.pop(self.combat.enemy_in_combat_index)
        self.combat = None

    def create_enemy_group(self, enemies_name_list,x ,y):
        enemy_group = []
        for name in enemies_name_list:
            new_figther = self.create_figther(name, x, y)
            enemy_group.append(new_figther)
        
        #add crew to each one
        for enemy in enemy_group:
            for other_enemy in enemy_group:
                if enemy == other_enemy:
                    pass
                else:
                    enemy.crew.append(other_enemy)

        self.current_enemies.append(enemy_group)

    def create_ally_group(self, allies_name_list,x ,y):
        ally_group = []
        for name in allies_name_list:
            new_figther = self.create_figther(name, x, y)
            ally_group.append(new_figther)
        
        #add crew to each one
        for ally in ally_group:
            for other_enemy in ally_group:
                if ally == other_enemy:
                    pass
                else:
                    ally.crew.append(other_enemy)

        return ally_group


#figure
class Figure(pygame.sprite.Sprite):
    def __init__(self, x, y, name, max_hp, strength, potions, scale, animation_list, height, crew=[], flipped=False, speed=10, animation_cooldown=130):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.scale = scale
        self.alive = True
        self.flipped = flipped
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0 #0: idle, 1: run
        self.update_time = p.time.get_ticks()
        self.x = x*SQ_SIZE
        self.y = y*SQ_SIZE - (self.animation_list[0][0].get_height())*(height -1) #hvis en figur ikke dukker opp på rett brikke se mer på dette
        self.goal_x = x*SQ_SIZE
        self.goal_y = y*SQ_SIZE - (self.animation_list[0][0].get_height())*(height -1) #hvis en figur ikke dukker opp på rett brikke se mer på dette
        self.animation_cooldown = animation_cooldown
        self.speed = speed
        self.running = False
        self.height = height
        self.rect = self.animation_list[0][0].get_rect()
        self.mask_image = p.mask.from_surface(self.animation_list[self.action][self.frame_index])
        self.mask_image = self.mask_image.to_surface()


        self.crew = [self] + crew

        #combat moves
        self.in_combat = False
        self.pos_before_fight = [x, y]
        self.combat_moves_list = []
        self.get_basic_move()


    def update(self):
        if self.hp <= 0:
            self.hp = 0
            self.alive = False


    def load_images(self, num_frames, action, file_format="png"):
        #load images
        pass

    def flipp(self):
        for i_a,action in enumerate(self.animation_list):
            for i_f, frame in enumerate(action):
                self.animation_list[i_a][i_f] = p.transform.flip(self.animation_list[i_a][i_f], True, False)



    def attack(self, target):
        pass

    def idle(self):
        self.action = 0
        if self.running:
            self.frame_index = 0
            self.running = False

    def run(self):
        self.action = 1
        if not self.running:
            self.frame_index = 0
            self.running = True


    def get_basic_move(self):
        self.combat_moves_list.append(CombatMove())
        self.combat_moves_list.append(CombatMove(0, 0, "Pass"))
        self.combat_moves_list.append(CombatMove(0, 0, "Run"))


class Combat:
    def __init__(self, allies, enemies,gs):
        self.enemy_in_combat_index = gs.current_enemies.index(enemies)
        print(self.enemy_in_combat_index)
        self.allies = allies
        self.enemies = enemies
        self.main_enemy =  self.enemies[0]
        self.allies_and_enemies = self.allies + self.enemies
        self.turn_index = 0
        self.target_index = 0
        self.turn = self.allies_and_enemies[0]
        self.target = self.get_first_enemy()
        self.ally_turn = True
        # self.turn_enemy_faces() #does not work atm


    def turn_enemy_faces(self):
        for enemy in self.enemies:
            enemy.flipp()

    def next_turn(self):
        self.turn_index += 1
        if self.turn_index >= len(self.allies_and_enemies):
            self.turn_index = 0
        self.turn = self.allies_and_enemies[self.turn_index]
        if self.turn in self.enemies: #enemy turn
            self.ally_turn = False
            self.target = self.allies[0]
        else: # ally turn
            if not self.ally_turn:
                self.ally_turn = True
                self.target = self.enemies[0]

    def get_first_enemy(self):
        for fighter in self.allies_and_enemies:
            if fighter in self.enemies:
                return fighter
        return self.enemies[0]
    
    def change_target(self, gs, location):
        for fighter in gs.combat.allies_and_enemies:
            fighter.rect.x = fighter.x
            fighter.rect.y = fighter.y
            if fighter.rect.collidepoint(location):
                gs.combat.target = fighter
                # self.ally_turn = True if fighter in self.allies else False # is the new turn an ally or enemy
        print(gs.combat.target.name)

    def run_combat(self):
        pass

    def move_hp_and_write(self, combat_move, font, gs):
        self.target.hp -= combat_move.damage
        self.turn.hp += combat_move.heal
        damage_text = DamageText(
            self.target.x , self.target.y + SQ_SIZE*(self.target.height - 1), str(combat_move.damage), p.color.Color("red"), font)
        heal_text = DamageText(
            self.turn.x, self.turn.y + SQ_SIZE*(self.turn.height - 1), str(combat_move.heal), p.color.Color("green"), font)
        gs.damage_text_group = p.sprite.Group()
        if combat_move.damage != 0:
            gs.damage_text_group.add(damage_text)
        if combat_move.heal != 0:
            gs.damage_text_group.add(heal_text)
        self.next_turn()


class CombatMove:
    def __init__(self, damage=100, heal=0, move_name="Kick"):
        self.name = move_name
        self.damage = damage
        self.heal = heal


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.created = p.time.get_ticks()