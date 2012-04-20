#!/usr/bin/env python

# Script to generate the u, by Beatrice Straile
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('u')

pen = glyph.getPen()

pen.moveTo((25,50))
pen.lineTo((25,500))
pen.lineTo((200,500))
pen.lineTo((200,75))
pen.lineTo((250,25))
pen.lineTo((300,10))
pen.lineTo((375,0))
pen.lineTo((425,25))
pen.lineTo((475,75))
pen.lineTo((475,275))
pen.lineTo((500,275))
pen.lineTo((500,150))
pen.lineTo((525,75))
pen.lineTo((575,25))
pen.lineTo((650,0))
pen.lineTo((175,0))
pen.lineTo((175,475))
pen.lineTo((100,400))
pen.lineTo((75,325))
pen.lineTo((50,225))
pen.closePath()


font.save()

