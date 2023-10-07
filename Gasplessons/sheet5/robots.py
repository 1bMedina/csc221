from gasp import *
from random import randint
from time import sleep


class RobotsGame:
    LEFT_KEY = "a"
    UP_LEFT_KEY = "q"
    UP_KEY = "w"
    UP_RIGHT_KEY = "e"
    RIGHT_KEY = "d"
    DOWN_RIGHT_KEY = "x"
    DOWN_KEY = "s"
    DOWN_LEFT_KEY = "z"
    TELEPORT_KEY = "t"
    RIGHT_EDGE = 63
    LEFT_EDGE = 0
    TOP_EDGE = 47
    BOTTOM_EDGE = 0

    def __init__(self):
        begin_graphics()
        self.finished = False
        self.player = Player()
        self.robot = Robot()

    def next_move(self):
        self.player.move()
        self.robot.move(self.player)
        # self.player.check_collisions(self.robot)

    def over():
        end_graphics()


class Player:
    def __init__(self):
        self.place()

    def place(self):
        self.x = randint(RobotsGame.LEFT_EDGE, RobotsGame.RIGHT_EDGE)
        self.y = randint(RobotsGame.BOTTOM_EDGE, RobotsGame.TOP_EDGE)
        self.shape = Circle((10 * self.x, 10 * self.y), 5, filled=True)

    def teleport(self):
        remove_from_screen(self.shape)
        self.place()

    def move(self):
        key = update_when("key_pressed")

        while key == RobotsGame.TELEPORT_KEY:
            self.teleport()
            key = update_when("key_pressed")

        if key == RobotsGame.RIGHT_KEY and self.x < RobotsGame.RIGHT_EDGE:
            self.x += 1
        elif key == RobotsGame.DOWN_RIGHT_KEY:
            if self.x < RobotsGame.RIGHT_EDGE:
                self.x += 1
            if self.y > RobotsGame.BOTTOM_EDGE:
                self.y -= 1
        elif key == RobotsGame.DOWN_KEY and self.y > RobotsGame.BOTTOM_EDGE:
            self.y -= 1
        elif key == RobotsGame.DOWN_LEFT_KEY:
            if self.x > RobotsGame.LEFT_EDGE:
                self.x -= 1
            if self.y > RobotsGame.BOTTOM_EDGE:
                self.y -= 1
        elif key == RobotsGame.LEFT_KEY and self.x > RobotsGame.LEFT_EDGE:
            self.x -= 1
        elif key == RobotsGame.UP_LEFT_KEY:
            if self.x > RobotsGame.LEFT_EDGE:
                self.x -= 1
            if self.y < RobotsGame.TOP_EDGE:
                self.y += 1
        elif key == RobotsGame.UP_KEY and self.y < RobotsGame.TOP_EDGE:
            self.y += 1
        elif key == RobotsGame.UP_RIGHT_KEY:
            if self.x < RobotsGame.RIGHT_EDGE:
                self.x += 1
            if self.y < RobotsGame.TOP_EDGE:
                self.y += 1

        move_to(self.shape, (10 * self.x, 10 * self.y))


class Robot:
    def __init__(self):
        self.place()

    def place(self):
        self.x = randint(RobotsGame.LEFT_EDGE, RobotsGame.RIGHT_EDGE)
        self.y = randint(RobotsGame.BOTTOM_EDGE, RobotsGame.TOP_EDGE)
        self.shape = Box((10 * self.x, 10 * self.y), 10, 10, filled=True, color="Red")

    def move(self, player):
        if self.x < player.x:
            self.x += 1
        elif self.x > player.x:
            self.x -= 1


        if self.y < player.y:
            self.y += 1
        elif self.y > player.y:
            self.y -= 1
        
        if self.y == player.y and self.x == player.x:
            game.finished = True
            print("Game Over")
            time.sleep(2)


        

        move_to(self.shape, (10 * self.x, 10 * self.y))


game = RobotsGame()

while not game.finished:
    game.next_move()
   
game.over()

