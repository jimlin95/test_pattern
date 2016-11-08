#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import argparse
import Image
import ImageDraw
# Definition
CANVAS_X = (1440)
CANVAS_Y = (1440)
START_X = (720)
START_Y = (720)
BOX_WIDTH = (50)
BOX_SPACING = (10)
INDEX_START = (1.0)
NUM_BOXS = (4)
OUTLINE_OFFSET = (10)
LINE_WIDTH = (3)
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
parser.add_argument('--pattern_rgb', '-p',
                    default='w',
                    choices=['r', 'g', 'b', 'w', 'R', 'G', 'B', 'W'],
                    help="Number of Boxs of each row")
parser.add_argument('--outline_width', '-b',
                    default=OUTLINE_OFFSET,
                    type=int,
                    help="The offset of outline")
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
    pattern_width = (args.num_boxs * args.box_width) + \
        args.box_spacing * (args.num_boxs - 1)
    pattern_half = pattern_width/2
    if args.verbose:
        print(pattern_width, pattern_half)
    start_x = start_x-pattern_half
    start_y = start_y-pattern_half
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
    # left line
    lux = start_x - args.outline_width - LINE_WIDTH
    luy = start_y - args.outline_width - LINE_WIDTH
    ldx = start_x - args.outline_width - LINE_WIDTH
    ldy = start_y + pattern_width + args.outline_width + LINE_WIDTH
    draw.line((lux, luy, ldx, ldy),
              fill=(255, 255, 255), width=LINE_WIDTH)
    # top line
    lux = start_x - args.outline_width - LINE_WIDTH
    luy = start_y - args.outline_width - LINE_WIDTH
    ldx = start_x + pattern_width + args.outline_width + LINE_WIDTH
    ldy = start_y - args.outline_width - LINE_WIDTH
    draw.line((lux, luy, ldx, ldy),
              fill=(255, 255, 255), width=LINE_WIDTH)
    # right line
    lux = start_x + pattern_width + args.outline_width+LINE_WIDTH
    luy = start_y - args.outline_width - LINE_WIDTH
    ldx = start_x + pattern_width + args.outline_width + LINE_WIDTH
    ldy = start_y + pattern_width + args.outline_width + LINE_WIDTH
    draw.line((lux, luy, ldx, ldy),
              fill=(255, 255, 255), width=LINE_WIDTH)
    # down line
    lux = start_x - args.outline_width - LINE_WIDTH
    luy = start_y + pattern_width + args.outline_width + LINE_WIDTH
    ldx = start_x + pattern_width + args.outline_width + LINE_WIDTH
    ldy = start_y + pattern_width + args.outline_width + LINE_WIDTH
    draw.line((lux, luy, ldx, ldy),
              fill=(255, 255, 255), width=LINE_WIDTH)


def merge(a, b):
    images = map(Image.open, [a, b])
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('test.png')


def main():
    im = create_canvas()
    draw = ImageDraw.Draw(im)
    draw_color_box(draw)
    im.save(args.outfile)
    merge(args.outfile, args.outfile)


if __name__ == '__main__':
    main()
