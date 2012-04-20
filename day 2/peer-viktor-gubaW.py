#!/usr/bin/env python

# Script to generate the w, by Peer Viktor Guba
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('w')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

pen.moveTo((175,400))
pen.lineTo((250,0))
pen.lineTo((350,530))
pen.lineTo((475,-150))
pen.lineTo((630,750))
pen.lineTo((590,750))
pen.lineTo((475,-100))
pen.lineTo((350,582))
pen.lineTo((250,55))
pen.lineTo((210,400))

pen.closePath()

font.save()
