#!/usr/bin/env python

# Script to generate the m, by Tobias Hahn

from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('m')

pen = glyph.getPen()

pen.moveTo((100,0))
pen.lineTo((100,480))
pen.lineTo((260,480))
pen.lineTo((260,320))
pen.lineTo((420,480))
pen.lineTo((580,480))
pen.lineTo((580,320))
pen.lineTo((740,480))
pen.lineTo((900,480))
pen.lineTo((900,0))
pen.lineTo((740,0))
pen.lineTo((740,320))
pen.lineTo((580,160))
pen.lineTo((580,0))
pen.lineTo((420,0))
pen.lineTo((420,320))
pen.lineTo((260,160))
pen.lineTo((260,0))
pen.closePath()

font.save()

