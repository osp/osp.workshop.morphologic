#!/usr/bin/env python

# Script to generate the question, by Raymin Chen
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('question')

pen = glyph.getPen()

pen.moveTo((250,000))
pen.lineTo((250,025))
pen.lineTo((275,025))
pen.lineTo((275,000))
pen.lineTo((250,000))
pen.closePath()

pen.moveTo((250,050))
pen.lineTo((275,050))
pen.lineTo((275,075))
pen.lineTo((300,075))
pen.lineTo((300,100))
pen.lineTo((325,100))
pen.lineTo((325,150))
pen.lineTo((300,150))
pen.lineTo((300,150))
pen.lineTo((300,175))
pen.lineTo((225,175))
pen.lineTo((225,150))
pen.lineTo((200,150))
pen.lineTo((200,125))
pen.lineTo((225,125))
pen.lineTo((225,150))
pen.lineTo((300,150))
pen.lineTo((300,100))
pen.lineTo((275,100))
pen.lineTo((275,075))
pen.lineTo((250,075))
pen.lineTo((250,050))

pen.closePath()

font.save()

