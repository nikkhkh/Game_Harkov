import pygame as pg
from player import Player

HEIGHT = 800
WEIGHT = 800

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((HEIGHT, WEIGHT))
        self.back_surf = pg.image.load('sources/back.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)

    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick()

    def draw(self):
        self.screen.blit(self.back_surf, (0, 0))
        self.player.draw()

    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT():
                pg.quit()

        keys = pg.key.get_pressed()
        self.player.move(keys)

    def update(self):
        pg.display.update()

game = Game()
game.game