from robofab.world import CurrentFont
from fontTools.misc.transform import Identity
import sys
import math

#matrix = Identity
#matrix = matrix.rotate(.25 * math.pi)

# rotatian is in radian (360 degrees = 2 * pi radians)
# you can also use: math.radians(45)

font = CurrentFont()

font.info.familyName = "JoTi"
font.info.styleName = "variant 3"
font.info.fullName = font.info.familyName + "-" + font.info.styleName


for glyph in font:
    pen = glyph.getPen()
    pen.moveTo((0,500))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,450))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,-200))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,-200))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,700))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,700))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,600))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,600))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,100))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,100))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,400))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,400))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,300))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,300))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,200))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,200))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,-100))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,-100))
    pen.closePath()
    
    pen = glyph.getPen()
    pen.moveTo((0,50))
    pen.lineTo((glyph.width,500))
    pen.lineTo((glyph.width,450))
    pen.lineTo((0,50))
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