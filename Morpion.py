import time

import Utils
from Bot import Bot
from Message import Message
from Player import Player
from Pos import Pos


class Morpion:

    def __init__(self):
        self.players = []
        # Make bigger or smaller board
        self.morpion_size = 3
        self.board = []
        self.indexer = {}
        # Init 2D array
        y = 0
        x = 0
        i = 1
        for row in range(0, self.morpion_size):
            self.board.append([])
            for column in range(0, self.morpion_size):
                self.board[row].append(str(i))
                self.indexer[i] = Pos(y, x)
                i += 1
                x += 1
            x = 0
            y += 1

        self.current_player = 0
        self.waiting_for_player()
        self.start_game()

    def start_game(self):
        self.display_info(True)
        self.waiting_for_action()

    # display the right symbol
    def set_symbol(self, y, x, symbol):
        self.board[y][x] = symbol

    def get_current_player(self):
        return self.players[self.current_player]

    def display_borders(self):
        # adapt with size
        s = " -"
        for i in range(self.morpion_size * 6):
            s += "-"
        print(s)

    def display_info(self, turn):
        # clear the console
        for i in range(0, 100):
            print("")
        # used for end game or not
        if turn:
            name = self.get_current_player().name
            print((Message.PLAYER_TURN.format(name)))
        print("\n")
        print(Message.DISPLAY_BOARD)
        x = 0
        y = 0
        for row in self.board:
            self.display_borders()
            for index in row:
                # check last pos of each row and display '|'
                display_line = " |  " + str(index) if (x < self.morpion_size - 1) else " |  " + str(index) + "  |"
                print(display_line, end=" ")
                x += 1
            x = 0
            y += 1
            print(end="\n")

        self.display_borders()



    def next_player(self):
        print(self.indexer)
        old_player = self.get_current_player()
        old_player.add_counter()

        # only start the check win algo after x actions (3 size)
        if old_player.counter >= self.morpion_size:
            if Utils.is_winner(self.board, old_player.symbol):
                self.display_info(False)
                print(Message.WON.format(old_player.name))
                self.ask_playing_again()
                return
            else:
                # check if end without winner
                if old_player.counter > self.morpion_size + 1:
                    self.display_info(False)
                    print(Message.NO_WINNER)
                    self.ask_playing_again()
                    return
        # next player
        self.current_player += 1
        if self.current_player > len(self.players) - 1:
            self.current_player = 0

        # display with player turns
        self.display_info(True)
        player = self.get_current_player()

        # check if it's bot
        if isinstance(player, Bot):
            # create fake thinking (lol robot are faster than human)
            print(Message.BOT_THINKING)
            time.sleep(2)

            # fill symbol
            i = player.action(self.indexer, self.board, False)
            pos = self.indexer[i]
            self.set_symbol(pos.y,
                            pos.x,
                            self.get_current_player().symbol)
            pos.player = self.current_player
            self.next_player()
        else:
            self.waiting_for_action()


    def ask_playing_again(self):
        answer = ""
        while answer == "":
            answer = input(Message.PLAY_AGAIN)
            if answer == "yes" or answer == 'y':
                Morpion()
                return
            elif answer == "no" or answer == 'n':
                break
            else:
                answer = ""


    def waiting_for_action(self):
        position = None
        while position == None:
            # check for int
            try:
                user_input = input(Message.ENTER_POSITION)
                index = int(user_input)

                # Easter egg
                if index == 42:
                    print("42 le sens de la vie... Vous remportez la victoire !")
                    self.ask_playing_again()
                    return

                # Real pos ?
                if self.indexer.__contains__(index):
                    # Check if pos is free
                    pos = self.indexer[index]
                    if pos.player < 0:
                        position = pos
                    else:
                        print(Message.POS_NOT_FREE)

                else:
                    print(Message.POS_NOT_FOUND)
            except ValueError:
                print(Message.MUST_BE_NUMBER)

        # fill symbol
        self.set_symbol(position.y,
                        position.x,
                        self.get_current_player().symbol)
        position.player = self.current_player

        self.next_player()


    def waiting_for_player(self):
        player_name = ""
        while player_name == "":
            player_number = len(self.players)
            is_first_player = player_number <= 0
            message = Message.ADD_PLAYER.format("X" if is_first_player else "O")
            player_name = input(message)

            if player_name == "":
                player_name = ""
                continue

            # Display bot available & check if player name is not already registered
            if not is_first_player:
                print(Message.BOT)
                contain = False
                for other in self.players:
                    if other.name == player_name:
                        contain = True
                        break
                if contain:
                    player_name = "";
                    print("Ce pseudo est déjà enregistré, veuillez en saisir un autre: ")
                    continue
                if player_name == "bot":
                    bot = Bot()
                    self.players.append(bot)
                    break

            p = Player(player_name)
            self.players.append(p)
            p.symbol = "X" if len(self.players) == 1 else "O"

            if player_number > 0:
                break;
            else:
                player_name = ""

