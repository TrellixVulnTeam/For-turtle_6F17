from math import sqrt

def heron(a, b, c): 
    s=(a+b+c)/2 
    return sqrt(s * (s - a) * (s - b) * (s - c))

print("Площадь трегольника со сторонами 3,4,5 =",heron(3,4,5))
