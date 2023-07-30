from settings import *
import json

class GameState():
    def __init__(self):
        # self.board_under = [["1, 4" for x in range(DIMENSION)] for x in range(DIMENSION)]
        # self.board_upper = [["--" for x in range(DIMENSION)] for x in range(DIMENSION)]
        self.curr_map = "start"
        self.load_current_map()

    def load_current_map(self):
        with open(f"data/maps/{self.curr_map}.json", "r") as infile:
            dic =json.load(infile)
            self.board_under = dic["under"]
            self.board_upper = dic["upper"]

