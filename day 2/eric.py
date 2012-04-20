#!/usr/bin/env python

# Script to generate the B, by Eric Schrijver

from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('B')

pen = glyph.getPen()

pen.moveTo((200,600))
pen.lineTo((600,650))
pen.lineTo((600,400))
pen.lineTo((400,300))
pen.lineTo((600,250))
pen.lineTo((600,0))
pen.lineTo((200,0))
pen.closePath()

pen.moveTo((300,550))
pen.lineTo((300,400))
pen.lineTo((450,400))
pen.lineTo((450,550))
pen.closePath()

pen.moveTo((300,200))
pen.lineTo((300,50))
pen.lineTo((450,50))
pen.lineTo((450,200))
pen.closePath()

font.save()

