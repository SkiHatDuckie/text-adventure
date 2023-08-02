import pygame as py
import pygame.freetype as py_freetype

from button import Button
from color import *
from scenebase import SceneBase
from text import draw_text


# The main game scene
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.font_vt323_24 = py_freetype.Font("assets\\fonts\\VT323-Regular.ttf", 24)

    def process_input(self, events, pressed_keys, pressed_mouse):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen_width, screen_height = screen.get_size()

        screen.fill(BG_COLOR1)
        draw_text(screen, self.game_title, FG_COLOR,
                  (10, 10, screen_width - 10, screen_height - 10),
                  self.font_vt323_24)
