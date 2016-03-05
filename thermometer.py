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

import senseSuppLib
import time

from sense_hat import SenseHat

def main():
    sense = SenseHat()
    sense.low_light = True
    print( "<---- Thermometer ---->\n" )
    # Get both available temperature values and compute their average
    temperature = min( int( ( sense.get_temperature_from_humidity() + sense.get_temperature_from_pressure() ) / 2 ), 128 )
    print( "The temperature is {0} degree Celsius".format( temperature ) )
    # Initialize the 'screen'
    backgroundHeader = senseSuppLib.LoadPixelStatusFromBIDF( "BIDF/thermoHeader.bidf" )
    senseSuppLib.UpdatePixelsFromPixelMatrix( [ 0, 127, 126 ], backgroundHeader, sense )
    backgroundMatrix = senseSuppLib.LoadPixelStatusFromBIDF( "BIDF/thermoBackground.bidf" )
    senseSuppLib.UpdatePixelsFromPixelMatrix( [ 0, 255, 0 ], backgroundMatrix, sense )
    # Print the binar-ized temperature (maximum 64 degrees Celsius)
    for i in range( 8 ):
        if temperature >= pow( 2, 7 - i ):
            sense.set_pixel( i, 6, [ 255, 255, 255 ] )
            temperature -= pow( 2, 7 - i )
    time.sleep( 30 )
    sense.clear()

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
