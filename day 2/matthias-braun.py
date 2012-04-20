#!/usr/bin/env python

# Script to generate the a, by Matthias Braun
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['a']
except KeyError:
    glyph = font.newGlyph('a')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

