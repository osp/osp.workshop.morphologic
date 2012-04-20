from robofab.world import RFont

font = RFont("NimbusSanL-Regu.ufo")

new = font.newGlyph("Space")
pen = new.getPointPen()

for glyph in [font['a'], font['b'], font['C']]:
    for contour in glyph:
    	print "start", glyph.name
        pen.beginPath()
        for point in contour.points:
            #if point.type == "offcurve" 
            pen.addPoint(point)
            print point
        pen.endPath()

new.update()
font.update()
