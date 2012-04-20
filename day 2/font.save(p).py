
# Script to generate the p, by Eva Maria Strecker

from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('p')

pen = glyph.getPen()


pen.moveTo((125,-250))
pen.lineTo((125,425))
pen.lineTo((150,475))
pen.lineTo((175,500))
pen.lineTo((450,500))
pen.lineTo((475,475))
pen.lineTo((500,425))
pen.lineTo((500,275))
pen.lineTo((475,225))
pen.lineTo((450,200))
pen.lineTo((250,200))
pen.lineTo((250,275))
pen.lineTo((450,275))
pen.lineTo((450,425))
pen.lineTo((200,425))
pen.lineTo((200,-250))
pen.lineTo((125,-250))
pen.closePath()


font.save()