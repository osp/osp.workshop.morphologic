#!/usr/bin/env python2
# usage: $ python2 print-font-robofab.py League-Gothic.ufo
from robofab.world import RFont
import sys
font = RFont(sys.argv[1])
for glyph in font:
    print glyph.name
