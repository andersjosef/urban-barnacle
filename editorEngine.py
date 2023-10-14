from settings import *
import json

class GameState():
    def __init__(self):
        # self.board_under = [["1, 4" for x in range(DIMENSION)] for x in range(DIMENSION)]
        # self.board_upper = [["--" for x in range(DIMENSION)] for x in range(DIMENSION)]
        self.map_dict = {}
        self.curr_level = "1"
        self.curr_map = "0, 0"
        self.load_current_map()

    def load_current_map(self, level="1", map="0, 0"):
        with open(f"data/maps/test.json", "r") as infile:
            dic =json.load(infile)
            self.map_dict = dic
            board = dic[level][map]
            self.board_under = board["under"]
            self.board_upper = board["upper"]

