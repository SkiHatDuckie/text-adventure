import pygame as py


# Draw some text into an area of a surface.
# Automatically wraps words.
# Returns any text that didn't get blitted.
def draw_text(surface, text, color, rect, font):
    rect = py.Rect(rect)
    y = rect.top
    line_spacing = -2

    # Get the height of the font
    font_height = font.render("Tg")[1][1]

    while text:
        i = 1

        # Determine if the row of text will be outside our area
        if y + font_height > rect.bottom:
            break

        # Determine maximum width of line
        while font.render(text[:i])[1][0] < rect.width and i < len(text):
            i += 1

        # If we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # Render the line and blit it to the surface
        image = font.render(text[:i], fgcolor=color)

        surface.blit(image[0], (rect.left, y))
        y += font_height + line_spacing

        # Remove the text we just blitted
        text = text[i:]

    return text