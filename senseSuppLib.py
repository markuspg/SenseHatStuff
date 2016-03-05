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

def CharToColour( argChar ):
    # Any character being non-'X' will be treated as a blank pixel
    if argChar != 'X':
        return [ 0, 0, 0 ]
    else:
        return [ 255, 255, 255 ]

def LoadImageFromBIDF( argPath ):
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
                imageMatrix.append( CharToColour( char ) )
            if len( imageMatrix ) % 8 != 0:
                imageMatrix.extend( [ [ 0, 0, 0 ] for i in range( 8 - len( imageMatrix ) % 8 ) ] )
    assert len( imageMatrix ) == 64
    return imageMatrix

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
