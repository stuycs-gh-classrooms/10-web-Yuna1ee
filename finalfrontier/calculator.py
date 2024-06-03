#! /usr/bin/python
print('Content-type: text/html\n')
#stats
#trig
#logs
#sequences
#solve rational functions

def quadratic (a, b, c): #returns roots of a quadratic
    #abc from string
    ans = ''
    x0 = 0
    x1 = 0
    discriminant = ((b ** 2) - (4 * a * c)) ** (1/2)
    left = (-1 * b) / (2 * a)
    right = 0
    if discriminant < 0:
        return 'no roots'
    else:
        right = discriminant / (2 * a)
        x0 = str(left + right)
        x1 = str(left - right)
    ans = 'The solutions are: ' + 'x = ' + x0 + ' and x = ' + x1
    return ans
    
def         
        
    