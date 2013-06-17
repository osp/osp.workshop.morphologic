#!/usr/bin/env python

from robofab.world import RFont

font = RFont()
font.info.familyName = "Morphologic"
font.info.styleName = "Regular"
font.info.postscriptFullName = font.info.familyName + ' ' + font.info.styleName
font.info.postscriptFontName = font.info.familyName + '-' + font.info.styleName
font.info.ascender = 750
font.info.descender = -250
font.info.xHeight = 500
font.info.capHeight = 750
font.info.unitsPerEm = 1000

font.save('Morphologic.ufo')

