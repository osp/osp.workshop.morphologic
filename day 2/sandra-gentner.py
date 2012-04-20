#!/usr/bin/env python

# Script to generate the l, by Sandra Gentner
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['l']
except KeyError:
    glyph = font.newGlyph('l')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

