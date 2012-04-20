#!/usr/bin/env python

# Script to generate the v, by Felix Marvin Vetter
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('v')

pen = glyph.getPen()

pen.moveTo((0,500))
pen.lineTo((150,500))
pen.lineTo((375,200))
pen.lineTo((600,500))
pen.lineTo((750,500))
pen.lineTo((375,0))
pen.lineTo((0,500))
pen.lineTo((0,500))
pen.closePath()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

