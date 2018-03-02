import math

def make_translate( x, y, z ):
    m=new_matrix(4,4)
    i=ident(m)
    m[3]=[x,y,z,1.0]
    return m

def make_scale( x, y, z ):
    m=new_matrix(4,4)
    i=ident(m)
    m[0]=[x,0.0,0.0,0.0]
    m[1]=[0.0,y,0.0,0.0]
    m[2]=[0.0,0.0,z,0.0]
    m[3]=[0.0,0.0,0.0,1.0]
    return m

def make_rotX( theta ):
    m=new_matrix(4,4)
    i=ident(m)
    rad=math.radians(theta) ##angle in radians
    cosa=math.cos(rad)
    sina=math.sin(rad)
    m[0]=[1.0,0.0,0.0,0.0]
    m[1]=[0.0,cosa,sina,0.0]
    m[2]=[0.0,sina*-1,cosa,0.0]
    m[3]=[0.0,0.0,0.0,1.0]
    return m
    
def make_rotY( theta ):
    m=new_matrix(4,4)
    i=ident(m)
    rad=math.radians(theta) ##angle in radians
    cosa=math.cos(rad)
    sina=math.sin(rad)
    m[0]=[cosa,0.0,sina*-1,0.0]
    m[1]=[0.0,1.0,0.0,0.0]
    m[2]=[sina,0.0,cosa,0.0]
    m[3]=[0.0,0.0,0.0,1.0]
    return m

def make_rotZ( theta ):
    m=new_matrix(4,4)
    i=ident(m)
    rad=math.radians(theta) ##angle in radians
    cosa=math.cos(rad)
    sina=math.sin(rad)
    m[0]=[cosa,sina,0.0,0.0]
    m[1]=[sina*-1,cosa,0.0,0.0]
    m[2]=[0.0,0.0,1.0,0.0]
    m[3]=[0.0,0.0,0.0,1.0]
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1.0
            else:
                matrix[c][r] = 0.0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0.0 )
    return m

###TEST
#print_matrix(make_translate(1,2,3))
#print make_translate(1,2,3)
#print make_scale(1,2,3)
#print print_matrix(make_rotZ(30))
