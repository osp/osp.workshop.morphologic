#!/usr/bin/env python

# Script to generate the percent, by Joana von Fuchs
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['percent']
except KeyError:
    glyph = font.newGlyph('percent')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

