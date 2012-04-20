from robofab.world import CurrentFont

font = CurrentFont()

lib = ["a","b","C"]
for g in [glyph.name for glyph in font]:
    old = font[g]
    print len(old)
    new = font.newGlyph("dummytmp", clear=True)
    
    pen = new.getPointPen()
    for contour in old:
        pen.beginPath()
        for point in contour.points:
            if point.type != "offCurve":
                pen.addPoint((point.x,point.y),"line")
        pen.endPath()
    
    font.newGlyph(g, clear=True)
    old.appendGlyph(new)
    print len(new)

font.update()