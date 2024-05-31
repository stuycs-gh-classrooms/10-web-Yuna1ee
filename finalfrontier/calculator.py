#! /usr/bin/python
print('Content-type: text/html\n')

def quadratic (string):
    string = string.replace(' ', '')
    splitters = ['+', '-']
    for splitter in splitters:
        string = string.split(splitter)
        string = ' '.join(string)
    string = string.split(' ')
    
    return string
s = '2x2 + 3x + 1'
print(quadratic(s))