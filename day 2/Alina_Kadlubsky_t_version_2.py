#!/usr/bin/env python

# Script to generate the t, by Alina Kadlubsky
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('t')

pen = glyph.getPen()

pen.moveTo((375,0))
pen.lineTo((250,0))
pen.lineTo((175,250))
pen.lineTo((175,475))
pen.lineTo((100,475))
pen.lineTo((100,525))
pen.lineTo((175,525))
pen.lineTo((175,750))
pen.lineTo((250,750))
pen.lineTo((250,525))
pen.lineTo((425,525))
pen.lineTo((425,475))
pen.lineTo((250,475))
pen.lineTo((250,250))
pen.lineTo((275,75))
pen.lineTo((375,75))
pen.lineTo((450,175))
pen.lineTo((500,175))

pen.closePath()

font.save()