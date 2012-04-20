#!/usr/bin/env python

# Script to generate the exclam, by Madlen GÃ¶hring
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('exclam')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

pen.moveTo((160,750))
pen.lineTo((340,750))
pen.lineTo((260,175))
pen.lineTo((235,175))
pen.closePath()

pen.moveTo((210,125))
pen.lineTo((290,125))
pen.lineTo((310,90))
pen.lineTo((310,40))
pen.lineTo((290,0))
pen.lineTo((210,0))
pen.lineTo((190,40))
pen.lineTo((190,90))
pen.closePath()

font.save()