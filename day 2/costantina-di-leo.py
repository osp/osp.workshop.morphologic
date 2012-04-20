#!/usr/bin/env python

# Script to generate the s, by Costantina Di Leo
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('s')

pen = glyph.getPen()

pen.moveTo((100,0))
pen.lineTo((200,0))
pen.lineTo((300,100))
pen.lineTo((300,200))
pen.lineTo((125,375))
pen.lineTo((125,400))
pen.lineTo((150,425))
pen.lineTo((250,425))
pen.lineTo((275,400))
pen.lineTo((300,450))
pen.lineTo((250,500))
pen.lineTo((125,500))
pen.lineTo((50,425))
pen.lineTo((50,350))
pen.lineTo((225,175))
pen.lineTo((225,125))
pen.lineTo((175,75))
pen.lineTo((100,75))
pen.lineTo((75,100))
pen.lineTo((50,50))
pen.closePath()


font.save()

