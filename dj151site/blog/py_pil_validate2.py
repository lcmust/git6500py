#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import Image
import ImageDraw
import ImageFont
import ImageFilter
import os
import string

class CreateValidateCode():
    _letter_cases = "abcdefghjkmnpqrstuvwxy"
    _upper_cases = _letter_cases.upper()
    _numbers = ''.join(map(str, range(3,10)))
    _init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
    #FONT_PATH = "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf"
    _font_path = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

    def __init__(self,
                 size = (120, 30),
                 chars = _init_chars,
                 img_type = "GIF",
                 mode = "RGB",
                 bg_color = (255, 255, 255),
                 fg_color = (0, 120, 240),
                 fg_color_random = 0,
                 font_size = 19,
                 font_type = _font_path, #"/share/fonts/truetype/freefont/FreeMono.ttf",
                 length = (4, 5),
                 draw_lines = True,
                 n_line = (1, 3),
                 draw_points = True,
                 point_chance = 2):
        self.size = size
        self.width, self.height = size
        self.chars = self._init_chars
        self.font_size = font_size
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.fg_color_random = fg_color_random
        self.font_type = font_type
        self.chars_length = length
        self.img = Image.new(mode, size, bg_color)
        self.draw = ImageDraw.Draw(self.img)
        self.n_line = n_line
        self.point_chance = point_chance
        self.draw_lines = draw_lines
        self.draw_points = draw_points

    def get_chars(self):
        self.chars_len = random.randint(*self.chars_length)
        return random.sample(self.chars, self.chars_len)

    def create_lines(self):
        self.line_num = random.randint(*self.n_line)

        for i in range(self.line_num):
            begin = (random.randint(0, self.size[0]),
                     random.randint(0, self.size[1]))
            end = (random.randint(0, self.size[0]),
                   random.randint(0, self.size[1]))
            self.draw.line([begin, end], fill = (110, 110, 110))

    def create_points(self):
        chance = min(100, max(0, int(self.point_chance)))

        for w in xrange(self.width):
            for h in xrange(self.height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    self.draw.point((w, h), fill = (0, 0, 0))

    def create_strs(self):
        c_chars = self.get_chars()
        strs = ' %s ' % ' '.join(c_chars)

        font = ImageFont.truetype(self.font_type, self.font_size)
        font_width, font_hight = font.getsize(strs)
        if self.fg_color_random:
            random_tmp = random.randint(1, 3)
            if random_tmp == 1:
                self.fg_color = (random.randint(100, 190),
                                 140,
                                 240
                                 )
            elif random_tmp == 2:
                self.fg_color = (100,
                                 random.randint(200, 220),
                                 240
                                 )
            else:
                self.fg_color = (100,
                                 240,
                                 random.randint(100, 200)
                                 )

        self.draw.text(((self.width - font_width) / 3,
                        (self.height - font_hight) / 3),
                       strs,
                       font = font,
                       fill = self.fg_color)
        return ''.join(c_chars)

    def create_all(self):
        if self.draw_lines:
            self.create_lines()
        if self.draw_points:
            self.create_points()
        self.strs = self.create_strs()

        self.params = [1 - float(random.randint(1, 2)) / 100,
                       0,
                       0,
                       0,
                       1 - float(random.randint(1, 10)) / 100,
                       float(random.randint(1, 2)) / 400,
                       0.001,
                       float(random.randint(1, 2)) / 400
                       ]
        """
        #上面这个参数params部分不正确，使用它时程序会报错：out list range
        #暂时不用，学习下PIL之后再调试
        """
        self.img = self.img.transform(self.size, Image.PERSPECTIVE, self.params)
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        return self.img, self.strs

if __name__ == "__main__":
    create1 = CreateValidateCode(fg_color_random=1)
    code_img, code_str = create1.create_all()
    code_img.save("/tmp/validate.gif", "GIF")
    print code_str
    code_img.show()
