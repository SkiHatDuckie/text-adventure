import pygame as py
import pygame.freetype as py_freetype

from button import Button
from character import *
from color import *
from scenebase import SceneBase
from text import draw_text


def next_dialogue(args) -> int:
    i = args[0]
    return i + 1


# The main game scene
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.font_vt323_24 = py_freetype.Font("assets\\fonts\\VT323-Regular.ttf", 24)

        self.player = Character("Ricky Rat", 20, 0,
                                (on_move_claws, on_move_bite, on_move_tail_whip))
        self.enemy = Character("None", 0, 0, ())

        self.combat = False

        self.dialogue_index = 0
        self.dialogue_text = (
            "Welcome to The Rat Chronicles Based Adventure DLC Part 2: A Spiced up Adventure \
we hope you enjoy this experience and will hope for another sequel to The Rat Chronicles.",
        )
        self.dialogue_options = (
            [
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ],
        )
        self.dialogue_option_args = (
            [self.dialogue_index],
        )

    def process_input(self, events, pressed_keys, pressed_mouse):
        for button in self.dialogue_options[self.dialogue_index]:
            button.check_for_hover()

        for event in events:
            if event.type == py.MOUSEBUTTONUP:
                if not self.combat:
                    for (i, button) in enumerate(self.dialogue_options[self.dialogue_index]):
                        self.dialogue_index = button.on_mouse_up(
                            self.dialogue_option_args[self.dialogue_index][i]
                        )

    def update(self):
        for button in self.dialogue_options[self.dialogue_index]:
            button.update()

    def render(self, screen):
        screen_width, screen_height = screen.get_size()

        screen.fill(BG_COLOR1)
        draw_text(screen, self.dialogue_text[self.dialogue_index], FG_COLOR,
                  (10, 10, screen_width - 20, screen_height - 70), self.font_vt323_24)

        for button in self.dialogue_options[self.dialogue_index]:
            button.render(screen)
