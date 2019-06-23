import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/1", "1_enemies_1_run_0" + add_str + ".png")),
        (64, 64)))


class Scorpion(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "scorpion"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]



