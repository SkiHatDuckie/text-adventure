import pygame as py


class Button:
    def __init__(self, text, font, fontColor, x, y, w, h, ic, ac, action):
        super().__init__()
        py.init()

        self.text = font.render(text, fgcolor=fontColor)

        self.x, self.y = x, y
        self.w, self.h = w, h
        self.ic = ic
        self.ac = ac
        self.rectColor = self.ic

        self.action = action
        self.hovered = False

    def check_for_hover(self):
        self.mPosX, self.mPosY = py.mouse.get_pos()
        if self.x <= self.mPosX <= (self.x + self.w) and self.y <= self.mPosY <= (self.y + self.h):
            self.hovered = True
        else:
            self.hovered = False

    def on_mouse_up(self, *args):
        if self.hovered:
            return self.action(args)

        return -1

    def update(self):
        if self.hovered:
            self.rectColor = self.ac
        else:
            self.rectColor = self.ic

    def render(self, screen):
        py.draw.rect(screen, self.rectColor, (self.x, self.y, self.w, self.h))

        textRect = self.text[1]
        textRect.center = (int(self.x+(self.w/2)), int(self.y+(self.h/2)))
        screen.blit(self.text[0], textRect)