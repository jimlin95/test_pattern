#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import argparse
import Image
import ImageDraw
# Definition
CANVAS_X = (1920)
CANVAS_Y = (1080)
START_X = (0)
START_Y = (0)
BOX_WIDTH = (50)
BOX_SPACING = (10)
INDEX_START = (1.0)
NUM_BOXS = (4)
OUTFILE = "test_pattern.png"
# args parser
# ---------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v',
                    default=0,
                    action='store_true',
                    help='verbose flag')
parser.add_argument('--outfile', '-o',
                    default=OUTFILE,
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
parser.add_argument('--canvas_x', '-c',
                    default=CANVAS_X,
                    type=int,
                    help="The width of Canvas")
parser.add_argument('--canvas_y', '-d',
                    default=CANVAS_Y,
                    type=int,
                    help="The hight  of Canvas")
parser.add_argument('--num_boxs', '-n',
                    default=NUM_BOXS,
                    type=int,
                    help="Number of Boxs of each row")
parser.add_argument('--pattern_r', '-r',
                    default=NUM_BOXS,
                    type=int,
                    help="Number of Boxs of each row")
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
    index = INDEX_START
    unit_div = (255.0)/((num_boxs**2)-1)
    print(unit_div)
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
            if args.verbose:
                print("color={}".format(color_fill))
            draw.rectangle(cor, fill=(color_fill, color_fill, color_fill, 255))
            index = index + 1
            print(index)


def main():
    im = create_canvas()
    draw = ImageDraw.Draw(im)
    draw_color_box(draw)
    im.save(args.outfile)
if __name__ == '__main__':
    main()
