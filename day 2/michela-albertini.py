#!/usr/bin/env python

# Script to generate the g, by Michela Albertini
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('g')

pen = glyph.getPen()

pen.moveTo((225,0))
pen.lineTo((100,125))
pen.lineTo((100,375))
pen.lineTo((225,500))
pen.lineTo((375,500))
pen.lineTo((500,375))
pen.lineTo((500,500))
pen.lineTo((650,500))
pen.lineTo((650,400))
pen.lineTo((600,400))
pen.lineTo((600,-50))
pen.lineTo((225,-150))
pen.lineTo((225,-175))
pen.lineTo((550,-175))
pen.lineTo((650,-75))
pen.lineTo((650,-150))
pen.lineTo((550,-250))
pen.lineTo((125,-250))
pen.lineTo((125,-100))
pen.lineTo((500,0))
pen.lineTo((500,125))
pen.lineTo((375,0))
pen.closePath()

pen.moveTo((275,100))
pen.lineTo((325,100))
pen.lineTo((400,175))
pen.lineTo((400,325))
pen.lineTo((325,400))
pen.lineTo((275,400))
pen.lineTo((200,325))
pen.lineTo((200,175))
pen.closePath()

font.save()
