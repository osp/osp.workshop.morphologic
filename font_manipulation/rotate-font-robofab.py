#!/usr/bin/env python2
# usage: $ rotate-font-robofab.py League-Gothic.ufo League-Gothic-tranformed.ufo
from robofab.world import RFont
from fontTools.misc.transform import Identity
import sys
import math
matrix = Identity
matrix = matrix.rotate(.25 * math.pi)
#math.radians(45)
font = RFont(sys.argv[1])
for glyph in font:
    glyph.transform(matrix)
font.save(sys.argv[2])
