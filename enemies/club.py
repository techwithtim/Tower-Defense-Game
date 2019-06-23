import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/5", "5_enemies_1_run_0" + add_str + ".png")).convert_alpha(),
        (64, 64)))


class Club(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "club"
        self.money = 5
        self.imgs = imgs[:]
        self.max_health = 5
        self.health = self.max_health



