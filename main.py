from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0  , 255, 0 ]
edges=[]
transform = new_matrix()

##Mr. Dw's Script
parse_file( 'script', edges, transform, screen, color )

##My Script:
color = [ 243, 243, 21 ]
edges=[]
parse_file( 'script2', edges, transform, screen, color )
