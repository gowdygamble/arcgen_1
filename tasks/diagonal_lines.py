import random

from tasks.task_utils.utils import *

import visualize
colors = visualize.colors


def diagonal_lines():
    h, w = random_canvas_shape(10,20, 10, 20)
    # select random background color here
    output_canvas = generate_blank(h, w)
    input_canvas = generate_blank(h, w)

    # generate colors
    background_color = 0

    number_of_lines = random.randint(1,3)
    used_colors = random.sample(list(range(1,len(colors))), number_of_lines)
    
    # identify endpoints

    for l in range(number_of_lines):
        z = []
        while len(z) < 3:
            z = generate_line_points(h,w)
        

        for i, point in enumerate(z):
            if i == 0 or i == len(z)-1:
                input_canvas[point[0]][point[1]] = used_colors[l]
            output_canvas[point[0]][point[1]] = used_colors[l]

        # color input + output

    

   


    return input_canvas, output_canvas

def generate_line_points(h, w, minLength=3, maxLength=6):

    startPoint = [random.randint(0,h-1), random.randint(0,w-1)]
    lineLength = random.randint(minLength, maxLength)
    points = [startPoint]

    directions = [[1,1], [-1,1], [1,-1], [-1,-1]]
    direction = random.choice(directions)

    for i in range(lineLength - 1):
        newPoint = list(points[-1])
        newPoint[0] += direction[0]
        newPoint[1] += direction[1]
        if newPoint[0] < 0 or newPoint[0] > h-1:
            break
        if newPoint[1] < 0 or newPoint[1] > w-1:
            break
        points.append(newPoint)
    return points



def task_func():
    i, o = diagonal_lines()
    return i, o



