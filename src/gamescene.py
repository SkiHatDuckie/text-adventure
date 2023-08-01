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
        self.game_title = "Testing, testing, 1 2 3"

        self.button_pressed_text = "Button clicked!"
        self.text_visible = False
        self.test_button = Button("Click me!", self.font_vt323_24, FG_COLOR, 10, 100, 100, 50,
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
        screen_width, screen_height = screen.get_size()

        screen.fill(BG_COLOR1)
        draw_text(screen, self.game_title, FG_COLOR,
                  (10, 10, screen_width - 10, screen_height - 10),
                  self.font_vt323_24)
        self.test_button.render(screen)
        if self.text_visible:
            draw_text(screen, self.button_pressed_text, FG_COLOR, (150, 100, 300, 300),
                      self.font_vt323_24)
