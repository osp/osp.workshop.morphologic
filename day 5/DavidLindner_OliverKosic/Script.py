from robofab.world import CurrentFont
from fontTools.misc.transform import Identity
import sys
import math


matrix = Identity
matrix2 = Identity
matrix3 = Identity
matrix4 = Identity
matrix2 = matrix.rotate(math.radians(-3))
matrix = matrix.rotate(math.radians(-8))
matrix3 = matrix.rotate(math.radians(5))
matrix4 = matrix.rotate(math.radians(6))
matrix5 = matrix.rotate(math.radians(-6))
matrix6 = matrix.rotate(math.radians(8))


font = CurrentFont()



for letter1 in [font['B'], font['V'], font['Z'], font['J'], font['I'], font['O'],font['U'], font['A'],font['two'], font['four']]:
    letter1.transform(matrix)
    letter1.update()  
    pen = letter1.getPen()
    pen.moveTo((-90,125))
    pen.lineTo((293,420))
    pen.lineTo((637,614))
    pen.lineTo((311,375)) 
    pen.closePath()
    pen.moveTo((194,648))
    pen.lineTo((264,552 ))
    pen.lineTo((615,81))
    pen.lineTo((263,523)) 
    pen.closePath()
    
  
for letter2 in [font['a'], font['u'], font['i'], font['n'], font['c'], font['j'],font['o'], font['e'],font['five'], font['three']]:
    letter2.transform(matrix2)
    letter2.update()  
    pen = letter2.getPen()
    pen.moveTo((-90,-125))
    pen.lineTo((218,262))
    pen.lineTo((385,488))
    pen.lineTo((283,322)) 
    pen.closePath()
   
for letter3 in [font['m'], font['k'], font['b'], font['p'], font['q'], font['w'],font['S'], font['z'],font['six'], font['one']]:
    letter3.transform(matrix3)
    letter3.update()  
    pen = letter3.getPen()
    pen.moveTo((-66,247))
    pen.lineTo((348,164))
    pen.lineTo((740,60))
    pen.lineTo((393,111)) 
    pen.closePath()   
    pen.moveTo((656,282))
    pen.lineTo((455,198))
    pen.lineTo((230,68))
    pen.lineTo((509,200)) 
    pen.closePath()
    
for letter4 in [font['W'], font['D'], font['Q'], font['K'], font['G'], font['X'],font['R'], font['N'], font['P'],font['d'], font['T'],font['zero'], font['nine']]:
    letter4.transform(matrix4)
    letter4.update()  
    pen = letter4.getPen()
    pen.moveTo((17,1075))
    pen.lineTo((102,556))
    pen.lineTo((338,-59))
    pen.closePath()
    pen.moveTo((-81,325))
    pen.lineTo((284,458))
    pen.lineTo((740,603))
    pen.lineTo((315,433)) 
    pen.closePath()
    
for letter5 in [font['t'], font['l'], font['f'], font['r'], font['v'],font['seven'], font['eight']]:
    letter5.transform(matrix5)
    letter5.update()  
    pen = letter5.getPen()
    pen.moveTo((-68,247))
    pen.lineTo((73,199))
    pen.lineTo((329,60))
    pen.closePath()   
    pen.moveTo((267,551))
    pen.lineTo((118,400))
    pen.lineTo((-118,17))
    pen.closePath()

for letter6 in [font['C'], font['E'], font['F'], font['H'], font['L'],font['Y'], font['g'], font['h'], font['s'], font['x'], font['y']]:
    letter6.transform(matrix6)
    letter6.update()  
    pen = letter6.getPen()
    pen.moveTo((470,745))
    pen.lineTo((343,533))
    pen.lineTo((172,120))
    pen.closePath()   
 



font.update()

