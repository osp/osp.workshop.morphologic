#!/usr/bin/env python

# Script to generate the r, by Jule Hartmann

from robofab.world import RFont
font = RFont('Morphologic.ufo')



glyph = font.newGlyph('r')

pen = glyph.getPen()


pen.moveTo((125,0))
pen.lineTo((200,0))
pen.lineTo((250,225))
pen.lineTo((325,0))
pen.lineTo((400,0))
pen.lineTo((260,300))
pen.lineTo((275,350))
pen.lineTo((600,350))
pen.lineTo((600,450))
pen.lineTo((400,575))
pen.lineTo((275,575))
pen.lineTo((100,450))
pen.lineTo((100,275))
pen.lineTo((150,275))
pen.lineTo((150,375))
pen.lineTo((200,375))
pen.closePath()

pen.moveTo((425,325))
pen.lineTo((275,325))
pen.lineTo((275,500))
pen.lineTo((425,500))
pen.closePath()

font.save()



