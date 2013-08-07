#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import Image
import ImageDraw
import ImageFont
import ImageFilter
import os
import string

_letter_cases = "abcdefghjkmnpqrstuvwxy"
_upper_cases = _letter_cases.upper()
_numbers = ''.join(map(str, range(3,10)))
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
#FONT_PATH = "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf"
FONT_PATH = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

def create_validate_code(size = (120, 30), chars = init_chars,
                         img_type = "GIF", mode = "RGB",
                         bg_color = (255, 255, 255),
                         fg_color = (0, 0, 255),
                         font_size = 22,
                         font_type = FONT_PATH, #"/usr/share/fonts/truetype/freefont/FreeMono.ttf",
                         length = 4, draw_lines = True,
                         n_line = (1, 3), draw_points = True,
                         point_chance = 2):
    width, height = size
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)

    def get_chars():
        return random.sample(chars, length)

    def create_lines():
        line_num = random.randint(*n_line)

        for i in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill = (0, 0, 0))

    def create_points():
        chance = min(100, max(0, int(point_chance)))

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill = (0, 0, 0))

    def create_strs():
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars)

        font = ImageFont.truetype(font_type, font_size)
        font_width, font_hight = font.getsize(strs)

        draw.text(((width - font_width) / 3, (height - font_hight) / 3),
                  strs, font = font, fill = fg_color)
        return ''.join(c_chars)

    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()

    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    #上面这个参数params部分不正确，使用它时程序会报错：out list range
    #暂时不用，学习下PIL之后再调试
    #img = img.transform(size, Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img, strs

if __name__ == "__main__":
    code_img, code_text = create_validate_code()
    code_img.save("/tmp/validate.gif", "GIF")
    print code_text
    code_img.show()
