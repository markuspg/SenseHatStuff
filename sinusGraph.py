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

from math import cos, sin
from sense_hat import SenseHat
from senseSuppLib import UpdateScreen
from time import sleep

def main():
    sense = SenseHat()
    sense.low_light = True
    print( "<---- SinusGraph ---->\n" )
    pixelStatuses = [ [ 0, 0, 0 ] for i in range( 64 ) ]
    for i in range( 150 ):
        assert len( pixelStatuses ) == 64
        del pixelStatuses[ : 8 ]
        pixelStatuses.extend( [ [ 0, 0, 0 ] for i in range( 8 ) ] )
        pixelStatuses[ 60 + round( cos( i / 1.5 ) * 3 ) ] = [ 0, 255, 0 ]
        pixelStatuses[ 60 + round( sin( i / 2 ) * 3 ) ] = [ 255, 255, 255 ]
        sense.set_pixels( pixelStatuses )
        pixelStatuses = sense.get_pixels()
        print( pixelStatuses )
        sleep( 0.096 )
    sense.clear()

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
