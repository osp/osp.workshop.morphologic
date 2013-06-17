from robofab.world import RFont
font = RFont('Morphologic.ufo')

for glyph in font:
    if glyph.isEmpty() != True:
        minX,minY,maxX,maxY = glyph.box
        glyph.width = maxX+minX

font.save()