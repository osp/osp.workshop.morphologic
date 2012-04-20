#!/usr/bin/env python

# Script to generate the y, by Oliver Kosic
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('y')

pen = glyph.getPen()
pen.moveTo((0,500))
pen.lineTo((150,500))
pen.lineTo((475,35))
pen.lineTo((715,375))
pen.lineTo((600,375))
pen.lineTo((600,500))
pen.lineTo((950,500))
pen.lineTo((285,-450))
pen.lineTo((100,-450 ))
pen.lineTo((100,-300))
pen.lineTo((240,-300))
pen.lineTo((400,-71))
pen.closePath()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

