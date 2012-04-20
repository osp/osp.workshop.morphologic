#!/usr/bin/env python

# Script to generate the j, by Dino Alexander Carasso
from robofab.world import RFont
font = RFont('Morphologic.ufo')

#try:
#    glyph = font['j']
#except KeyError:
glyph = font.newGlyph('j')

pen = glyph.getPen()

pen.moveTo((125,550))
pen.lineTo((200,550))
pen.lineTo((200,525))
pen.lineTo((125,450))
pen.closePath()

pen.moveTo((200,500))
pen.lineTo((200,-150))
pen.lineTo((150,-200))
pen.lineTo((25,-200))
pen.lineTo((100,-125))
pen.lineTo((125,-125))
pen.lineTo((125,425))
pen.closePath()

font.save()

