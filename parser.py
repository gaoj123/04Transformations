from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    done=False
    f=open(fname,"r")
    lines=f.readlines()
    i=0
    while i<len(lines):
        if done==True:
            break
        indexOfLine=i
        for l in lines:
            lines[lines.index(l)]=l.strip("\n")
        line=lines[i]
        if line=="line":
            nextLine=lines[indexOfLine+1] ##get arguments
            args=nextLine.split()  ##split arguments by space
            for a in args:
                if a.isdigit():
                    args[args.index(a)]=int(a)
            add_edge(points,args[0],args[1],args[2],args[3],args[4],args[5])
            i+=2
        elif line=="ident":
            ident(transform) ##turns transform matrix into identity matrix
            clear_screen(screen)
            i+=1
        elif line=="scale":
            nextLine=lines[indexOfLine+1] ##get arguments
            args=nextLine.split()
            for a in args:
                if a.isdigit():
                    args[args.index(a)]=int(a)
            scale=make_scale(args[0],args[1],args[2])
            matrix_mult(scale,transform)
            i+=2
        elif line=="move":
            nextLine=lines[indexOfLine+1] ##get arguments
            args=nextLine.split()
            for a in args:
                if a.isdigit():
                    args[args.index(a)]=int(a)
            tr=make_translate(args[0],args[1],args[2])
            matrix_mult(tr,transform)
            i+=2
        elif line=="rotate":
            nextLine=lines[indexOfLine+1] ##get arguments
            args=nextLine.split()
            for a in args:
                if a.isdigit():
                    args[args.index(a)]=int(a)
            ro=new_matrix(4,4)
            axis=args[0]
            angle=args[1]
            if axis=="x":
                ro=make_rotX(angle)
            elif axis=="y":
                ro=make_rotY(angle)
            else:
                ro=make_rotZ(angle)
            matrix_mult(ro,transform)
            i+=2
        elif line=="apply":
            matrix_mult(transform,points)
            i+=1
        elif line=="display":
            draw_lines(points,screen,color)
            display(screen)
            i+=1
        elif line=="save":
            draw_lines(points,screen,color)
            nextLine=lines[indexOfLine+1] #get file name
            args=nextLine.split()
            save_extension(screen, args[0])
            i+=2
        elif line=="quit":
            done=True
        else:
            i+=1
   

