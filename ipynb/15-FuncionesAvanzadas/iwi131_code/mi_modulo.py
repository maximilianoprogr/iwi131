from math import pi, tan

def area_circulo(r):
    area = pi*r**2
    return area

def area_rectangulo(a,b):
    area = a*b
    return area

def area_cuadrado(a):
    return area_rectangulo(a,a)

def area_poligono(n, a):
    angulo = 2.*pi/n
    h = 0.5*a / tan(0.5*angulo)
    area_triangulo = 0.5*h*a
    area = n * area_triangulo
    return area
