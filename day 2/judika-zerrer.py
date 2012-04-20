#!/usr/bin/env python

# Script to generate the n, by Judika Zerrer
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['n']
except KeyError:
    glyph = font.newGlyph('n')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

