#!/usr/bin/env python

# Script to generate the i, by Stefania-Lea Antoniadou
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('i')

pen = glyph.getPen()

pen.moveTo((100,575))
pen.lineTo((200,575))
pen.lineTo((100,475))
pen.lineTo((100,575))
pen.closePath()

pen.moveTo((100,400))
pen.lineTo((200,500))
pen.lineTo((200,0))
pen.lineTo((100,-100))
pen.lineTo((100,400))
pen.closePath()

font.save()

