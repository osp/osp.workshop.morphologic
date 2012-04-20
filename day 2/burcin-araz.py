#!/usr/bin/env python

# Script to generate the z, by Burcin Araz
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['z']
except KeyError:
    glyph = font.newGlyph('z')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

