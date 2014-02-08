from itertools import combinations

def euclid(a, b):
    '''returns the Greatest Common Divisor of a and b'''
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def coprime(l):
    '''returns 'True' if the values in the list L are all co-prime
       otherwier, it returns 'False'. '''
    for i, j in combinations(l, 2):
        if euclid(i, j) != 1:
            return False
    return True

def extendedEuclid(a, b):
    '''return a tuple of three values: x, y and z, such that x is
    the GCD of a and b, and x = y * a + z * b'''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedEuclid(b % a, a)
        return (g, x - (b // a) * y, y)

print extendedEuclid(3,6)