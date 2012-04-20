#!/usr/bin/env python

# Script to generate the p, by Eva Maria Strecker
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['p']
except KeyError:
    glyph = font.newGlyph('p')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

