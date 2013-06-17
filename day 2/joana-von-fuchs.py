from robofab.world import RFont
font = RFont ('Morphologic.ufo')

try:
	glyph = font ['percent']
except KeyError:
	glyph = font.newGlyph ('percent')
	
pen = glyph.getPen()

pen.moveTo((225,100))
pen.lineTo((225,150))
pen.lineTo((475,400))
pen.lineTo((525,400))
pen.lineTo((525,350))
pen.lineTo((275,100))
pen.closePath()

font.save()

pen = glyph.getPen()

pen.moveTo((250,325))
pen.lineTo((225,350))
pen.lineTo((225,375))
pen.lineTo((250,400))
pen.lineTo((275,400))
pen.lineTo((300,375))
pen.lineTo((300,350))
pen.lineTo((275,325))
pen.closePath()

font.save()

pen = glyph.getPen()

pen.moveTo((475,100))
pen.lineTo((450,125))
pen.lineTo((450,150))
pen.lineTo((475,175))
pen.lineTo((500,175))
pen.lineTo((525,150))
pen.lineTo((525,125))
pen.lineTo((500,100))
pen.closePath()

font.save()
