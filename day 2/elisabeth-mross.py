#!/usr/bin/env python

# Script to generate the e, by Elisabeth Mross
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('e')

pen = glyph.getPen()

pen.moveTo((100,550))
pen.lineTo((550,550))
pen.lineTo((550,250))
pen.lineTo((150,250))
pen.lineTo((150,50))
pen.lineTo((550,50))
pen.lineTo((550,0))
pen.lineTo((100,0))
pen.closePath()

pen.moveTo((150,500))
pen.lineTo((150,300))
pen.lineTo((500,300))
pen.lineTo((500,500))
pen.closePath()


# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

