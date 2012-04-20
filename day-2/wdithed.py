from robofab.world import CurrentFont

font = CurrentFont()

for glyph in font:
    if glyph.isEmpty() != True:
        minX,minY,maxX,maxY = glyph.box
        glyph.width = maxX+minX

font.update()