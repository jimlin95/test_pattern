#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import argparse
import Image
# Definition
START_X = (0)
START_Y = (0)
BOX_WIDTH = (50)
BOX_SPACING = (10)
INDEX_START = (1.0)
NUM_BOXS = (4)
PROBE_WIDTH = (30)
INFILE = "test_pattern.png"
# args parser
# ---------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v',
                    default=0,
                    action='store_true',
                    help='verbose flag')
parser.add_argument('--infile', '-i',
                    default=INFILE,
                    help='Filename to  process')
parser.add_argument('--x_coor', '-x',
                    default=START_X,
                    type=int,
                    help="The X coordinate of start")
parser.add_argument('--y_coor', '-y',
                    default=START_Y,
                    type=int,
                    help="The Y coordinate of start")
parser.add_argument('--box_width', '-w',
                    default=BOX_WIDTH,
                    type=int,
                    help="The width of Box")
parser.add_argument('--box_spacing', '-s',
                    default=BOX_SPACING,
                    type=int,
                    help="The width between Boxs")
parser.add_argument('--num_boxs', '-n',
                    default=NUM_BOXS,
                    type=int,
                    help="Number of Boxs of each row")
parser.add_argument('--pattern_rgb', '-p',
                    default='w',
                    choices=['r', 'g', 'b', 'w', 'R', 'G', 'B', 'W'],
                    help="Number of Boxs of each row")
parser.add_argument('--probe_width', '-d',
                    default=PROBE_WIDTH,
                    type=int,
                    help="The width of probe")
args = parser.parse_args()
# ---------------------------------------------------------------------------


def create_canvas():
    canvas_x = args.canvas_x
    canvas_y = args.canvas_y
    im = Image.new("RGB", (canvas_x, canvas_y))
    return im


def draw_color_box(draw):
    start_x = args.x_coor
    start_y = args.y_coor
    num_boxs = args.num_boxs
    box_width = args.box_width
    box_spacing = args.box_spacing
    pattern_rgb = args.pattern_rgb
    index = INDEX_START
    unit_div = (255.0)/((num_boxs**2)-1)
    for y in range(start_y, start_y+(box_width+box_spacing)*num_boxs,
                   (box_width+box_spacing)):
        for x in range(start_x, start_x+(box_width+box_spacing)*num_boxs,
                       (box_width+box_spacing)):
            cor = (x, y, x+box_width, y+box_width)
            if args.verbose:
                print("(x,y,x2,y2)={}".format(cor))
            if index == INDEX_START:
                color_fill = 0
            elif index == (num_boxs**2):
                color_fill = 255
            else:
                color_fill = int((index-1) * unit_div)
            if pattern_rgb == 'w' or pattern_rgb == 'W':
                final_color = (color_fill, color_fill, color_fill, 255)
            if pattern_rgb == 'r' or pattern_rgb == 'R':
                final_color = (color_fill, 0, 0, 255)
            if pattern_rgb == 'g' or pattern_rgb == 'G':
                final_color = (0, color_fill, 0, 255)
            if pattern_rgb == 'b' or pattern_rgb == 'B':
                final_color = (0, 0, color_fill, 255)
            draw.rectangle(cor, fill=final_color)
            if args.verbose:
                print("final_color={}".format(final_color))
            index = index + 1


def probe_box(pix, x_start, y_start):
    box_sum_r = 0
    box_sum_g = 0
    box_sum_b = 0
    # print(x_start, y_start)
    for y in range(y_start, y_start + args.probe_width):
        for x in range(x_start, x_start + args.probe_width):
            r, g, b = pix[x, y]
            box_sum_r += r
            box_sum_g += g
            box_sum_b += b
            # print(x, y, r, g, b)

    return box_sum_r / (args.probe_width**2), \
        box_sum_g / (args.probe_width**2), \
        box_sum_b / (args.probe_width**2)


def color_cal(pix):
    start_y = args.y_coor
    stop_y = args.y_coor + (args.box_width + args.box_spacing) \
        * (args.num_boxs)
    step_y = args.box_width + args.box_spacing

    start_x = args.x_coor
    stop_x = args.x_coor + (args.box_width + args.box_spacing) \
        * (args.num_boxs)
    step_x = args.box_width + args.box_spacing

    # print(start_y, stop_y, step_y)
    # print(start_x, stop_x, step_x)
    for y in range(start_y, stop_y, step_y):
        for x in range(start_x, stop_x, step_x):
            all = probe_box(pix, x + (args.box_width - args.probe_width) / 2,
                            y + (args.box_width - args.probe_width) / 2)
            print("({},{}) = {}".format(x, y, all))


def main():
    im = Image.open(args.infile)
    pix = im.load()
    color_cal(pix)


if __name__ == '__main__':
    main()
