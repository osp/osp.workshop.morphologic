#!/usr/bin/env python

# Script to generate the q, by Matthias Mann
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['q']
except KeyError:
    glyph = font.newGlyph('q')

pen = glyph.getPen()

pen.moveTo((400,125))
pen.lineTo((175,125))
pen.lineTo((75,225))
pen.lineTo((75,375))
pen.lineTo((175,475))
pen.lineTo((400,475))
pen.lineTo((500,375))
pen.lineTo((500,225))
pen.lineTo((400,125))
pen.closePath()

pen.moveTo((175,175))
pen.lineTo((400,175))
pen.lineTo((450,225))
pen.lineTo((450,375))
pen.lineTo((400,425))
pen.lineTo((175,425))
pen.lineTo((125,375))
pen.lineTo((125,225))
pen.lineTo((175,175))
pen.closePath()

pen.moveTo((500,225))
pen.lineTo((500,125))
pen.lineTo((575,125))
pen.lineTo((575,25))
pen.lineTo((500,25))
pen.lineTo((500,-250))
pen.lineTo((450,-250))
pen.lineTo((450,25))
pen.lineTo((375,25))
pen.lineTo((375,75))
pen.lineTo((450,75))
pen.lineTo((450,175))
pen.lineTo((500,225))

pen.closePath()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

