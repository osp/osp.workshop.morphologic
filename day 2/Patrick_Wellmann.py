#!/usr/bin/env python

# Script to generate the K, by Patrick Wellmann

from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('k')

pen = glyph.getPen()

pen.moveTo((100,0))
pen.lineTo((100,500))
pen.lineTo((150,500))
pen.lineTo((150,300))
pen.lineTo((350,500))
pen.lineTo((400,500))
pen.lineTo((175,275))
pen.lineTo((400,50))
pen.lineTo((400,0))
pen.lineTo((150,250))
pen.lineTo((150,0))
pen.lineTo((100,0))
pen.closePath()

font.save()

