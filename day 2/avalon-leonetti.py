#!/usr/bin/env python

# Script to generate the b, by Avalon Leonetti
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('b')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

pen = glyph.getPen()

pen.moveTo((0,0))
pen.lineTo((25,100))
pen.lineTo((25,750))
pen.lineTo((110,750))
pen.lineTo((112,475))
pen.lineTo((112,475))
pen.lineTo((200,500))
pen.lineTo((300,500))
pen.lineTo((400,450))
pen.lineTo((450,350))
pen.lineTo((475,225))
pen.lineTo((450,125))
pen.lineTo((375,25))
pen.lineTo((275,0))
pen.lineTo((175,0))
pen.lineTo((100,25))
pen.lineTo((75,0))
pen.closePath()

pen.moveTo((113,432))
pen.lineTo((113,62))
pen.lineTo((250,50))
pen.lineTo((250,50))
pen.lineTo((350,125))
pen.lineTo((375,225))
pen.lineTo((325,400))
pen.lineTo((225,450))
pen.lineTo((175,450))

pen.closePath()


font.save()
