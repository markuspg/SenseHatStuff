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

from sense_hat import SenseHat

import random
import time

def main():
    # Initialization stuff
    sense = SenseHat()
    sense.low_light = True
    # Display a random pixel matrix
    pixelValues = [ [ random.randint( 0, 255 ) for j in range( 3 ) ] for i in range( 64 ) ]
    sense.set_pixels( pixelValues )
    time.sleep( 3 )
    # Create a colour 'beat'
    for i in range( 3 ):
        sense.clear( 255, 0, 0 )
        time.sleep ( 0.333 )
        sense.clear( 0, 255, 0 )
        time.sleep ( 0.333 )
        sense.clear( 0, 0, 255 )
        time.sleep ( 0.333 )
    # Toy around with text display
    message = "Einfach Mensch..."
    sense.show_message( message, 0.05 )
    rotation = 0
    for letter in message:
        sense.set_rotation( rotation, False )
        rotation += 90
        if rotation == 270:
            rotation = 0
        sense.show_letter( letter )
        time.sleep( 0.24 )
    sense.clear()

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
