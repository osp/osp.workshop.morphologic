from robofab.world import CurrentFont

font = CurrentFont()

for glyph in font:
    for contour in glyph:
        for point in contour.points:
            if point.type != "offCurve" and point.y == 0:
                point.y = point.y + 10

    font.update()

"""    old = font[g]
    print len(old)
    new = font.newGlyph("dummytmp", clear=True)
    
    pen = new.getPointPen()
    for contour in old:
        pen.beginPath()
        for point in contour.points:
            if point.type != "offCurve" and point.y == 0:
                pen.addPoint((point.x,point.y+10),point.type)
                print old.name, point.x, point.y , "modifiziert!"
            else:
                pen.addPoint((point.x,point.y), point.type)
        pen.endPath()
    
    font.newGlyph(g, clear=True)
    old.appendGlyph(new)

font.update()"""