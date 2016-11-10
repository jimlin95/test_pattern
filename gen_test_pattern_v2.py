#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import argparse
import Image
import ImageDraw
# Definition
CANVAS_X = (2880)
CANVAS_Y = (1440)
START_X1 = (760)
START_Y1 = (720)
START_X2 = (2160)
START_Y2 = (720)
BOX_WIDTH = (50)
BOX_SPACING = (10)
INDEX_START = (1.0)
NUM_BOXS = (4)
OUTLINE_OFFSET = (10)
LINE_WIDTH = (3)
LINE_COLOR = "white"
TEMPFILE = "pattern.png"
OUTFILE = "test_pattern.png"
PATTERN_NUM = (2)
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
parser.add_argument('--x1',
                    default=START_X1,
                    type=int,
                    help="The X1 coordinate of start")
parser.add_argument('--y1',
                    default=START_Y1,
                    type=int,
                    help="The Y1 coordinate of start")
parser.add_argument('--x2',
                    default=START_X2,
                    type=int,
                    help="The X2 coordinate of start")
parser.add_argument('--y2',
                    default=START_Y2,
                    type=int,
                    help="The Y2 coordinate of start")
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
parser.add_argument('--line_width', '-l',
                    default=LINE_WIDTH,
                    type=int,
                    help="The offset of outline")
args = parser.parse_args()
# ---------------------------------------------------------------------------


def create_canvas(canvas_x, canvas_y):
    im = Image.new("RGB", (canvas_x, canvas_y))
    return im


def draw_color_box(draw, num_boxs, box_width, box_spacing,
                   pattern_rgb, line_width):
    start_x = box_spacing + line_width
    start_y = box_spacing + line_width
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


def draw_box_outline(im, color, line_width):
    width, height = im.size
    draw = ImageDraw.Draw(im)
    cor = (line_width, line_width, width-1-line_width,
           height-1-line_width)  # (x1,y1, x2,y2)
    line = (cor[0], cor[1], cor[0], cor[3])
    draw.line(line, fill=color, width=line_width)
    line = (cor[0], cor[1], cor[2], cor[1])
    draw.line(line, fill=color, width=line_width)
    line = (cor[0], cor[3], cor[2], cor[3])
    draw.line(line, fill=color, width=line_width)
    line = (cor[2], cor[1], cor[2], cor[3])
    draw.line(line, fill=color, width=line_width)


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


def picture_canvas_prepare(nb, bw, sw, of, lw):
    y_w = x_w = nb * bw + (nb - 1) * sw + lw * 2 + 2 * of
    im = create_canvas(x_w, y_w)
    draw = ImageDraw.Draw(im)
    return im, draw


def pattern_paste(pattern_file, canvas, target, outputfile, num):
    img = Image.open(pattern_file, 'r')
    img_w, img_h = img.size
    background = Image.new('RGB', canvas)
    bg_w, bg_h = background.size
    if num == 1:
        target_x1, target_y1 = target
        background.paste(img, (target_x1-img_w/2, target_y1-img_h/2))
    elif num == 2:
        target_x1, target_y1, target_x2, target_y2 = target
        background.paste(img, (target_x1-img_w/2, target_y1-img_h/2))
        background.paste(img, (target_x2-img_w/2, target_y2-img_h/2))

    background.save(outputfile)


def main():
    num_boxs = args.num_boxs
    box_width = args.box_width
    box_spacing = args.box_spacing
    pattern_rgb = args.pattern_rgb
    outline_width = args.outline_width
    line_width = args.line_width
    im, draw = picture_canvas_prepare(num_boxs, box_width,
                                      box_spacing, outline_width, line_width)
    draw_color_box(draw, num_boxs, box_width, box_spacing, pattern_rgb,
                   line_width)
    draw_box_outline(im, LINE_COLOR, line_width)
    im.save(TEMPFILE)
    pattern_paste(TEMPFILE, (args.canvas_x, args.canvas_y),
                  (args.x1, args.y1, args.x2, args.y2),
                  args.outfile, PATTERN_NUM)


if __name__ == '__main__':
    main()
