#!/usr/bin/env python

# Script to generate the ampersand, by Tamara Hell
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('ampersand')

pen = glyph.getPen()

pen.moveTo((225,0))
pen.lineTo((175,50))
pen.lineTo((125,150))
pen.lineTo((225,300))
pen.lineTo((175,400))
pen.lineTo((275,550))
pen.lineTo((425,525))
pen.lineTo((475,375))
pen.lineTo((350,225))
pen.lineTo((425,150))
pen.lineTo((525,225))
pen.lineTo((500,250))
pen.lineTo((500,275))
pen.lineTo((625,275))
pen.lineTo((625,250))
pen.lineTo((550,200))
pen.lineTo((525,175))
pen.lineTo((425,100))
pen.lineTo((475,50))
pen.lineTo((550,25))
pen.lineTo((550,0))
pen.lineTo((450,0))
pen.lineTo((400,50))
pen.lineTo((375,0))
pen.closePath()

pen.moveTo((375,500))
pen.lineTo((275,500))
pen.lineTo((230,450))
pen.lineTo((275,325))
pen.lineTo((350,300))
pen.lineTo((425,375))
pen.closePath()

pen.moveTo((275,250))
pen.lineTo((175,150))
pen.lineTo((225,75))
pen.lineTo((325,50))
pen.lineTo((375,75))
pen.lineTo((325,225))
pen.closePath()
# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

