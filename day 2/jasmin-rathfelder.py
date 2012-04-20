#!/usr/bin/env python

# Script to generate the Euro, by Jasmin Rathfelder
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
    glyph = font['onesuperior']
except KeyError:
    glyph = font.newGlyph('onesuperior')

pen = glyph.getPen()

pen.moveTo((600,0))
pen.lineTo((350,250))
pen.lineTo((250,250))
pen.lineTo((150,350))
pen.lineTo((250,350))
pen.lineTo((225,375))
pen.lineTo((250,400))
pen.lineTo((150,400))
pen.lineTo((250,500))
pen.lineTo((350,500))
pen.lineTo((600,750))
pen.lineTo((700,650))
pen.lineTo((550,650))
pen.lineTo((425,500))
pen.lineTo((575,500))
pen.lineTo((675,400))
pen.lineTo((375,400))
pen.lineTo((350,375))
pen.lineTo((375,350))
pen.lineTo((675,350))
pen.lineTo((575,250))
pen.lineTo((425,250))
pen.lineTo((550,100))
pen.lineTo((700,100))
pen.closePath()

font.save()

