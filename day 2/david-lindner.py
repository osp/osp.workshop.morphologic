#!/usr/bin/env python

# Script to generate the d, by David Lindner
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('d')

pen = glyph.getPen()
pen.moveTo((0,0))
pen.lineTo((100,300))
pen.lineTo((325,300))
pen.lineTo((375,250))
pen.lineTo((350,175))
pen.lineTo((300,225))
pen.lineTo((175,225))
pen.lineTo((125,75))
pen.lineTo((350,75 ))
pen.lineTo((550,675))
pen.lineTo((625,600))
pen.lineTo((425,0))
pen.closePath()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

