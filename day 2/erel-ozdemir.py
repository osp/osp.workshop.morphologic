from robofab.world import RFont
font = RFont('Morphologic.ufo')


glyph = font.newGlyph('o')

pen = glyph.getPen()

pen.moveTo((125,0))
pen.lineTo((50,100))
pen.lineTo((50,400))
pen.lineTo((125,500))
pen.lineTo((325,500))
pen.lineTo((400,400))
pen.lineTo((400,100))
pen.lineTo((325,0))
pen.closePath()

pen.moveTo((162,12))
pen.lineTo((288,12))
pen.lineTo((350,88))
pen.lineTo((350,412))
pen.lineTo((288,488))
pen.lineTo((162,488))
pen.lineTo((100,412))
pen.lineTo((100,88))
pen.closePath()

font.save()