import random

def generate_blank(height, width, background_color=0):
    background = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(background_color)
        background.append(row)
    return background


def random_canvas_shape(heightMin, heightMax, widthMin, widthMax):
    return random.randint(heightMin, heightMax), random.randint(widthMin, widthMax)

def random_square_canvas_shape(sideMin, sideMax):
    s = random.randint(sideMin, sideMax)
    return s, s


