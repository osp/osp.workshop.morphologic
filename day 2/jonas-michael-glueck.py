#!/usr/bin/env python

# Script to generate the h, by Jonas Michael Glueck
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('h')

pen = glyph.getPen()

pen.moveTo((200,0))
pen.lineTo((200,700))
pen.lineTo((150,700))
pen.lineTo((100,750))
pen.lineTo((300,750))
pen.lineTo((300,500))
pen.lineTo((500,500))
pen.lineTo((600,400))
pen.lineTo((600,0))
pen.lineTo((500,0))
pen.lineTo((500,350))
pen.lineTo((450,400))
pen.lineTo((300,400))
pen.lineTo((300,0))
pen.closePath()

font.save()

