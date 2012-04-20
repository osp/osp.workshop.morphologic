from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
	glyph = font['z']
except KeyError:
	glyph = font.newGlyph ('z')
	
pen = glyph.getPen()

pen.moveTo((200,500))
pen.lineTo((200,400))
pen.lineTo((700,400))
pen.lineTo((700,500))
pen.closePath()

font.save()

pen = glyph.getPen()

pen.moveTo((675,375))
pen.lineTo((225,125))
pen.closePath()

font.save()

pen = glyph.getPen()

pen.moveTo((200,100))
pen.lineTo((200,0))
pen.lineTo((700,0))
pen.lineTo((700,100))
pen.closePath()

font.save()

