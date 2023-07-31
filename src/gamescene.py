import pygame.freetype as py_freetype

from scenebase import SceneBase
from color import *


# The main game scene
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        font_vt323_24 = py_freetype.Font("assets\\fonts\\VT323-Regular.ttf", 24)
        self.game_title = font_vt323_24.render("Testing, testing, 1 2 3", fgcolor=FG_COLOR)

    def processInput(self, events, pressed_keys, pressed_mouse):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill(BG_COLOR)
        screen.blit(self.game_title[0], (10, 10))