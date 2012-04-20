
from robofab.world import RFont
font = RFont('Morphologic.ufo')

try:
	glyph = font['n']
except KeyError:
	glyph = font.newGlyph ('n')

pen = glyph.getPen()

pen.moveTo((250,500))
pen.lineTo((325,500))
pen.lineTo((325,475))
pen.lineTo((600,475))
pen.lineTo((650,450))
pen.lineTo((675,400))
pen.lineTo((675,25))
pen.lineTo((750,0))
pen.lineTo((525,0))
pen.lineTo((600,25))
pen.lineTo((600,375))
pen.lineTo((575,425))
pen.lineTo((525,450))
pen.lineTo((325,450))
pen.lineTo((325,25))
pen.lineTo((400,0))
pen.lineTo((175,0))
pen.lineTo((250,25))
pen.lineTo((250,400))
pen.lineTo((175,425))
pen.closePath()

font.save()