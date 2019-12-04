import random

import Utils
from Player import Player


class Bot(Player):

    def __init__(self):
        super().__init__("Bot")
        self.symbol = "O"

    def action(self, indexer, board, hard):
        if hard:
            board_cloned = board
            # Idea Make 2 bots trying to win
            # TODO make the ai unbeatable
            pass
        else:
            # check for pos not filled by other player
            available_pos = []
            for key in indexer:
                pos = indexer[key]
                if pos.player < 0:
                    available_pos.append(key)
            # get random pos
            random_index = random.choice(available_pos)
            return random_index
        return -1