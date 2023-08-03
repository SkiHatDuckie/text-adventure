from button import *
from color import *


def next_dialogue(args) -> int:
    i = args[0]
    return i + 1


def next_dialogue_x2(args) -> int:
    i = args[0]
    return i + 2


def die_i_guess(args) -> int:
    return -1


class Dialogue:
    def __init__(self, text: str, *options):
        self.text = text
        self.options = options
