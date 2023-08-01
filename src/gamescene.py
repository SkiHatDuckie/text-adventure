import pygame as py
import pygame.freetype as py_freetype

from button import Button
from color import *
from scenebase import SceneBase


# The main game scene
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        font_vt323_24 = py_freetype.Font("assets\\fonts\\VT323-Regular.ttf", 24)
        self.game_title = font_vt323_24.render("Testing, testing, 1 2 3", fgcolor=FG_COLOR)

        self.button_pressed_text = font_vt323_24.render("Button clicked!", fgcolor=FG_COLOR)
        self.text_visible = False
        self.test_button = Button("Click me!", font_vt323_24, FG_COLOR, 10, 100, 100, 50,
                                  BG_COLOR1, BG_COLOR2)

    def process_input(self, events, pressed_keys, pressed_mouse):
        self.test_button.check_for_hover()
        for event in events:
            if event.type == py.MOUSEBUTTONUP:
                self.test_button.check_for_press()

    def update(self):
        self.test_button.update()
        if self.test_button.consume_pressed():
            self.text_visible = not self.text_visible

    def render(self, screen):
        screen.fill(BG_COLOR1)
        screen.blit(self.game_title[0], (10, 10))
        self.test_button.render(screen)
        if self.text_visible:
            screen.blit(self.button_pressed_text[0], (150, 100))
