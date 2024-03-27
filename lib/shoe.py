#!/usr/bin/env python3

class Shoe:

    def __init__( self, brand, size ) :

        self.brand = brand
        self.size = size

        # @property
        # def brand ( self ) :

        #     return self._brand
        
        @property
        def size ( self ) :

            return self._size
        
        
        # @brand.setter
        # def brand ( self, value ) :
            
        #     self._brand = value

        
        @size.setter
        def size ( self, value ) :

            if isinstance ( value, int ) :

                self._size = value
            else :
                print ( "size must be an integer" )


    def can_cobble ( self ) :

        return ( "The shoe has been repaired." )
        # print ( "Your shoe is as good as new!\n" )
    
    def cobble_makes_new ( self ) :

        self.condition = "New"
        # self = Shoe ( self.brand, self.size, self.condition )
    
