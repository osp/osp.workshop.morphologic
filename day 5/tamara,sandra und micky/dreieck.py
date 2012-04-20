#for name in [glyph.name for glyph in font]:
    

from robofab.world import RFont

font = RFont("URWGothicL-Book-console.ufo")

for glyph in font:
    if glyph.isEmpty() == False:
        pen = glyph.getPen()
    
        v = glyph.box[0]
        # entspricht x  ganz links unten
        x = glyph.box[1]
        # entspricht y ganz links unten
        y = glyph.box[2]
        # entspricht x oben rechts
        z = glyph.box[3]
        # entspricht y oben rechts
    
       
        pen.moveTo((y,x))
        pen.lineTo((y,z))
        pen.lineTo((v,z))
        pen.closePath()
    
        print glyph.box
 
font.save()