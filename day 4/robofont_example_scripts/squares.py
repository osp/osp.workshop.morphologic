# Source: http://robofab.com/talks09/printBooklet.html
# It is probably under the same license as Robofab, BSD

# robothon 2009
# rasterise the shape in glyph "A"
# and draw boxes in a new glyph named "A.silly"
#
 
from robofab.world import CurrentFont, CurrentGlyph, RGlyph

f = CurrentFont()

for glyph in ['a', 'b']:
    sourceGlyph = glyph
 
    source = f[sourceGlyph]
 
    # find out how big the shape is from the glyph.box attribute
    xMin, yMin, xMax, yMax = source.box
 
    # create a new glyph
    dest = f.newGlyph("silly")
    dest.width = source.width
 
    # get a pen to draw in the new glyph
    myPen = dest.getPen()
 
    # a function which draws a rectangle at a specified place
    def drawRect(pen, x, y, size=50):
        pen.moveTo((x-.5*size, y-.5*size))
        pen.lineTo((x+.5*size, y-.5*size))
        pen.lineTo((x+.5*size, y+.5*size))
        pen.lineTo((x-.5*size, y+.5*size))
        pen.closePath()
 
    # the size of the raster unit
    resolution = 30
 
    # draw from top to bottom
    yValues = range(int(yMin), int(yMax), resolution)
    yValues.reverse()
 
    # go for it!
    for y in yValues:
        for x in range(int(xMin), int(xMax), resolution):
            # check the source glyph is white or black at x,y
            if source.pointInside((x, y)):
                drawRect(myPen, x, y, resolution-5)
        # update for each line if you like the animation
        # otherwise move the update() out of the loop
        dest.update()
        print dest
    
    source = f.newGlyph(sourceGlyph, clear=True)
    source.appendGlyph(dest)

f.removeGlyph('silly')
f.update()
