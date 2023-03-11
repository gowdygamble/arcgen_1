import random

from tasks.task_utils.utils import *

import visualize
colors = visualize.colors





def fill_inner():
    h, w = random_canvas_shape(10,20, 10, 20)
    # select random background color here
    output_canvas = generate_blank(h, w)
    input_canvas = generate_blank(h, w)

    # generate colors
    background_color = 0
    fill_color = random.randint(1, len(colors) - 1)
    border_color = random.randint(1, len(colors) - 1)
    while border_color == fill_color:
        border_color = random.randint(1, len(colors) - 1)

    # define interior regions
    for i in range(3):
        pixelhole_r, pixelhole_c = generate_pixelhole_coords(h, w)
        output_canvas[pixelhole_r][pixelhole_c] = fill_color

    # color borders
    
    for r in range(h):
        for c in range(w):

            if output_canvas[r][c] == fill_color:
                #for r_offset in [-1, 1]:
                #for c_offset in [-1,1]:
                for offsets in [[-1,0],[1,0],[0,-1],[0,1]]:
                    r_offset, c_offset = offsets[0], offsets[1]
                    if output_canvas[r + r_offset][c + c_offset] == background_color:
                        output_canvas[r + r_offset][c + c_offset] = border_color
                        input_canvas[r + r_offset][c + c_offset] = border_color

    # AND CHECK FOR Missed interiors!
    # interiors created by nearby borders
    # basically flood fill

    # for r in range(h):
    #     for c in range(w):

    #         for offsets in [[-1,0],[1,0],[0,-1],[0,1]]:

    #         if output_canvas[r][c] == fill_color:
    #             #for r_offset in [-1, 1]:
    #             #for c_offset in [-1,1]:
                
    #                 r_offset, c_offset = offsets[0], offsets[1]
    #                 if output_canvas[r + r_offset][c + c_offset] == background_color:
    #                     output_canvas[r + r_offset][c + c_offset] = border_color
    #                     input_canvas[r + r_offset][c + c_offset] = border_color

    # some other random pixels?

    return input_canvas, output_canvas


def task_func():
    i, o = fill_inner()
    return i, o

def generate_pixelhole_coords(height, width):
    r = random.randint(1, height - 2)
    c = random.randint(1, width - 2)
    return r, c


# input, output = fill_inner()
# visualize.visualize_io_pair(input, output)


