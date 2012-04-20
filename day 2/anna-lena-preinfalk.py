#!/usr/bin/env python

# Script to generate the c, by Anna-Lena Preinfalk
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('c')

pen = glyph.getPen()

pen.moveTo((150,500))
pen.lineTo((600,500))
pen.lineTo((600,400))
pen.lineTo((250,400))
pen.lineTo((250,100))
pen.lineTo((600,100))
pen.lineTo((600,0))
pen.lineTo((150,0))
pen.closePath()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

