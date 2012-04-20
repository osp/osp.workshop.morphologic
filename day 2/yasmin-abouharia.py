#!/usr/bin/env python

# Script to generate the f, by Yasmin Abouharia
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('f')

pen = glyph.getPen()

pen.moveTo((300,0))
pen.lineTo((375,125))
pen.lineTo((400,725))
pen.lineTo((450,700))
pen.lineTo((425,675))
pen.lineTo((425,650))
pen.lineTo((450,625))
pen.lineTo((475,625))
pen.lineTo((500,650))
pen.lineTo((500,700))
pen.lineTo((475,725))
pen.lineTo((400,750))
pen.lineTo((300,575))
pen.lineTo((275,25))
pen.lineTo((250,100))
pen.lineTo((175,125))
pen.lineTo((150,75))
pen.lineTo((225,0))
pen.closePath()

pen.moveTo((250,450))
pen.lineTo((300,425))
pen.lineTo((475,450))
pen.closePath()

font.save()