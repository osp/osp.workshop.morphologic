#!/usr/bin/env python

# Script to generate the germandbls, by Jennifer Mantas
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['germandbls']
except KeyError:
    glyph = font.newGlyph('germandbls')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

