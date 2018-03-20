from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

#parse_file( 'script', edges, transform, screen, color )
'''
add_box(edges, 50, 50, 0, 100, 150, 50)
matrix_mult(make_rotX(45), edges)
matrix_mult(make_rotY(45), edges)
matrix_mult(make_translate(50, 100, 0), edges)
'''
add_sphere(edges, 250, 250, 0, 100, 100)
matrix_mult(make_rotY(45), edges)
clear_screen(screen)
draw_lines(edges, screen, color)
display(screen)

