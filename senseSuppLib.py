#!/usr/bin/env python3

##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of SenseHatStuff.
##
##  SenseHatStuff is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  SenseHatStuff is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with SenseHatStuff.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

def CharToPixel( argChar ):
    """
    Returns the pixel value 'True' (on) or 'False' (off) of the passed character
    """
    # Any character being non-'X' will be treated as a blank pixel
    if argChar != 'X':
        return False
    else:
        return True

def LoadPixelStatusFromBIDF( argPath ):
    """
    This returns a matrix of 64 'True'/'False' values loaded from the passed file
    """
    imageMatrix = list()
    with open( argPath, 'r' ) as fileHandle:
        for line in fileHandle:
            line = line.strip()
            # Ensure that the matrix will never be greater than 8x8 in size
            # fill missing fields with emptiness
            if len( imageMatrix ) == 64:
                break
            # If lines are to long, crop them
            for char in line[ : 8 ]:
                imageMatrix.append( CharToPixel( char ) )
            # Ensure that each line is exactly eight signs long
            if len( imageMatrix ) % 8 != 0:
                imageMatrix.extend( [ False for i in range( 8 - len( imageMatrix ) % 8 ) ] )
    if len( imageMatrix ) < 64:
        imageMatrix.extend( [ False for i in range( 64 - len( imageMatrix ) ) ] )
    assert len( imageMatrix ) == 64
    return imageMatrix

def StatusToColour( argColour, argStatus ):
    """
    Returns a colour value according to the passed status
    """
    # Any character being non-'X' will be treated as a blank pixel
    if argStatus == True:
        return argColour
    else:
        return [ 0, 0, 0 ]

def UpdateScreen( argColour, argPixelStatuses, argSense ):
    """
    Updates the entire screen according to the passed pixel statuses with the passed colour
    """
    colourMatrix = [ StatusToColour( argColour, i ) for i in argPixelStatuses ]
    argSense.set_pixels( colourMatrix )

def UpdatePixelsFromPixelMatrix( argColour, argMatrix, argSense ):
    """
    In contrast to the other 'Update'-function this only updates the 'True' pixels.

    This allows painting coloured screens by painting one colour after another
    """
    for i in range( max( 64, len( argMatrix ) ) ):
        if argMatrix[ i ] == True:
            column = i % 8
            row = int( i / 8 )
            argSense.set_pixel( column, row, argColour )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
