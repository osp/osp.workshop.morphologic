#!/usr/bin/env python

# Script to generate the x, by Lisa-Sarah Efeoglu
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('x')

pen = glyph.getPen()

pen.moveTo((100,-50))
pen.lineTo((150,-50))
pen.lineTo((500,500))
pen.closePath()

pen.moveTo((150,500))
pen.lineTo((200,500))
pen.lineTo((500,0))
pen.closePath()



# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()
