from robofab.world import CurrentGlyph, CurrentFont

glyph = CurrentGlyph()

for contour in glyph:
    print "CONTOUR"
    for segment in contour:
        print "segment "
        print segment.points