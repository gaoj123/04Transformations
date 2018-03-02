from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges=[]
#edges = [[0.0,0.0,0.0,1.0],[10.0,10.0,0.0,1]]
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
