#!/usr/bin/env python2

from robofab.world import RFont
import sys

font = RFont()
font.info.familyName = "Morphologic"
font.info.styleName = "Regular"
font.info.fullName = font.info.familyName + '-' + font.info.styleName
font.info.ascender = 1000
font.info.descender = 0
font.info.unitsPerEm = 1000

glyph = font.newGlyph('b')
glyph.width = 1000

pen = glyph.getPen()

pen.moveTo((100,100))
pen.lineTo((100,700))
pen.lineTo((150,700))
pen.lineTo((150,400))
pen.lineTo((700,400))
pen.lineTo((700,100))
pen.closePath()

font.save(sys.argv[1])

