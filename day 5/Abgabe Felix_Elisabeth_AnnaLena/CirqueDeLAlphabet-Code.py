from robofab.world import CurrentFont
from fontTools.misc.transform import Identity
import math

matrix = Identity
matrix = matrix.scale(x=1.1, y=0.9)
matrix = matrix.skew(0.05*math.pi,0.1*math.pi)

matrix2 = Identity
matrix2 = matrix2.scale(x=1.1, y=0.9)
matrix2 = matrix2.skew(0.05*math.pi,0.1*math.pi)
matrix2 = matrix2.rotate(0.1*math.pi)

# rotatian is in radian (360 degrees = 2 * pi radians)
# you can also use: math.radians(45)

font = CurrentFont()

font.info.familyName = "OSP Morph"
font.info.styleName = "Zirkus_OSP_REG"
font.info.fullName = "Zirkus_OSP_REG"
font.info.postscriptFontName = "Zirkus_OSP_REG"

print font.info.fullName

for buchstabe in [font['a'], font['c'], font['e'], font['g'],font['i'],font['k'],font['m'],font['o'],
font['q'],font['s'],font['u'],font['w'],font['y']]:
    buchstabe.transform(matrix)
    #xMin,yMin,xMax,yMax = buchstabe.box
    #buchstabe.width = xMax - xMin
    buchstabe.update()
    
for grobuchstabe in [font['A'], font['C'], font['E'], font['G'],font['I'],font['K'],font['M'],font['O'],
font['Q'],font['S'],font['U'],font['W'],font['Y']]:
    grobuchstabe.transform(matrix)
    #xMin,yMin,xMax,yMax = grobuchstabe.box
    #grobuchstabe.width = xMax - xMin
    grobuchstabe.update()
    
for buchstabe in [font['b'], font['d'], font['f'], font['h'],font['j'],font['l'],font['n'],font['p'],
font['r'],font['t'],font['v'],font['x'],font['z']]:
    buchstabe.transform(matrix2)
    buchstabe.move((20,0))
    #xMin,yMin,xMax,yMax = buchstabe.box
    #buchstabe.width = xMax - xMin
    buchstabe.update()
    
for grobuchstabe in [font['B'], font['D'], font['F'], font['H'],font['J'],font['L'],font['N'],font['P'],
font['R'],font['T'],font['V'],font['X'],font['Z']]:
    grobuchstabe.transform(matrix2)
    grobuchstabe.move((20,0))
    #xMin,yMin,xMax,yMax = grobuchstabe.box
    #grobuchstabe.width = xMax - xMin
    grobuchstabe.update()     
             
    

"""
Other insformations:
    
matrix.inverse           matrix.skew
matrix.transformPoints   matrix.reverseTransform
matrix.toPS              matrix.translate
matrix.rotate            matrix.transform         
matrix.scale             matrix.transformPoint    

"""