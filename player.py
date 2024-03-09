import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.bird_image = pg.image.load('sources/back.jpg')
        self.x = 400
        self.y = 400

    def draw(self):
        self.screen.blit(self.bird_image)

    def move(self, keys):
        if keys[pg.K_w]:
            self.y -= 10
        if keys[pg.K_s]:
            self.y += 10
        if keys[pg.K_a]:
            self.x -= 10
        if keys[pg.K_d]:
            self.x += 10
        

    def update(self):
        pass