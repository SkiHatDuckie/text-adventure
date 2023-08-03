import pygame as py
import pygame.freetype as py_freetype

from button import Button
from character import *
from color import *
from dialogue import *
from scenebase import SceneBase
from text import draw_text


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
        self.dialogues = (
            Dialogue(
                "Welcome to The Rat Chronicles Based Adventure DLC Part 2: A Spiced up \
Adventure we hope you enjoy this experience and will hope for another sequel to The Rat \
Chronicles.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "Ricky Rat is enjoying his bounty of stacks of ramen of the Rat King's den. \
They dance along the cavern incautiously, eventually coming upon a sack. This magical sack \
had astonished Ricky Rat with an inexplicable amount of ramen hidden in the sack.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "After stareing within the bag, the whole cavern suddenly shook.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "'KING RAT!!! SHOW YOURSELF!!!' Screeched a voice echoing through the cave. \
Quickly realizing that your only way out is through the voice, you snatched the bag and \
tried to sneak out of the cave.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "Upon reaching back to the entrance of King Rat's lair a squad of rats were \
in your way.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "There was 3 figure at the front, a white rat with scars on the tip of their \
nose, a black rat with red eyes with a bit of a twitch, and a gray chunky rat on a plastic blue \
wheelbarrow covering himself with red cheese dust.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50, BG_COLOR1,
                       BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "'Whose You? You ain't the Rat King' Yarred the white rat.",
                Button("\"I am so!\"", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50,
                       BG_COLOR1, BG_COLOR2, next_dialogue),
                Button("\"I'm just passing by\"", self.font_vt323_24, FG_COLOR, 120, 420, 210, 50,
                       BG_COLOR1, BG_COLOR2, next_dialogue_x2)
            ),
            Dialogue(
                "Suddenly a red and orange mist is covered around you, you feel the spices \
through your nose and eyes, The burn of the heat makes you pass out, GAME OVER",
                Button("Damn", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50,
                       BG_COLOR1, BG_COLOR2, die_i_guess)
            ),
            Dialogue(
                "'Are you now?! Well, aren't you just a regular old rat huh?', questions the \
white rat. 'The name's Salt, this is Pepper'', he points toward the black rat, 'And here's our \
Clan Master MSG', he points over to the oversized rat in a wheelbarrow.",
                Button("Next", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50,
                       BG_COLOR1, BG_COLOR2, next_dialogue)
            ),
            Dialogue(
                "'We're the Spice Packet Clan and looking for the Rat King for our ramen share, \
he's in there?', asks Salt Before you can even say another word some other rat yells about the \
sack that you're hiding behind your tail. 'Wait a minute, our reward! Rookie Cumin! Gettem!'",
                Button("Fight!", self.font_vt323_24, FG_COLOR, 10, 420, 100, 50,
                       BG_COLOR1, BG_COLOR2, next_dialogue)
            )
        )

    def process_input(self, events, pressed_keys, pressed_mouse):
        for button in self.dialogues[self.dialogue_index].options:
            button.check_for_hover()

        for event in events:
            if event.type == py.MOUSEBUTTONUP:
                if not self.combat:
                    new_index = self.dialogue_index
                    for button in self.dialogues[self.dialogue_index].options:
                        new_index = button.on_mouse_up(self.dialogue_index)
                        if new_index != None:
                            self.dialogue_index = new_index
                            break

    def update(self) -> int:
        if self.dialogue_index == -1:
            return -2  # Terminate app
        
        for button in self.dialogues[self.dialogue_index].options:
            button.update()

        return -1

    def render(self, screen):
        screen_width, screen_height = screen.get_size()

        screen.fill(BG_COLOR1)
        draw_text(screen, self.dialogues[self.dialogue_index].text, FG_COLOR,
                  (10, 10, screen_width - 20, screen_height - 70), self.font_vt323_24)

        for button in self.dialogues[self.dialogue_index].options:
            button.render(screen)
