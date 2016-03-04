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

import sys
import time

from sense_hat import SenseHat
from senseSuppLib import LoadImageFromBIDF

def main():
    sense = SenseHat()
    sense.low_light = True
    print( "<---- ImageDisplay ---->\n" )
    if len( sys.argv ) != 2:
        print( "There must be exactly one argument, the path of the to be displayed image" )
    else:
        print( "Displaying \'{0}\'".format( sys.argv[ 1 ] ) )
    imageMatrix = LoadImageFromBIDF( sys.argv[ 1 ] )
    sense.set_pixels( imageMatrix )
    time.sleep( 3 )
    sense.clear()

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
