from robofab.world import CurrentFont
from fontTools.misc.transform import Identity
import sys
import math

matrix = Identity
matrix = matrix.skew(.1 * math.pi)

# rotatian is in radian (360 degrees = 2 * pi radians)
# you can also use: math.radians(45)

font = CurrentFont()

for glyph in font:
    glyph.transform(matrix)

font.update()

"""
Other transformations:
    
matrix.inverse           matrix.skew
matrix.transformPoints   matrix.reverseTransform
matrix.toPS              matrix.translate
matrix.rotate            matrix.transform         
matrix.scale             matrix.transformPoint    

"""