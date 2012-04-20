from robofab.world import CurrentFont
from fontTools.misc.transform import Identity
import sys
import math

matrix = Identity
matrix = matrix.rotate(.25 * math.pi)

# rotatian is in radian (360 degrees = 2 * pi radians)
# you can also use: math.radians(45)

font = CurrentFont()

font.info.familyName = "JoTi"
font.info.styleName = "variant 1"
font.info.fullName = font.info.familyName + "-" + font.info.styleName

for glyph in font:
    
    pen = glyph.getPen()
    pen.moveTo((0,500))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,450))
    pen.closePath()
        
    pen = glyph.getPen()
    pen.moveTo((200,0))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,200))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((200,0))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,200))
    pen.closePath()
 
 #   glyph.transform(matrix)



font.update()

"""
Other transformations:
    
matrix.inverse           matrix.skew
matrix.transformPoints   matrix.reverseTransform
matrix.toPS              matrix.translate
matrix.rotate            matrix.transform         
matrix.scale             matrix.transformPoint    

"""