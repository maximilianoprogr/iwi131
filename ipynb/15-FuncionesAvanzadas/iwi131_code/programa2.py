import mi_modulo

def volumen_piramide(a, h):
    area_base = mi_modulo.area_cuadrado(a)
    volumen = area_base * h / 3.0
    return volumen

A = float(raw_input("Lado de la base cuadrada: "))
H = float(raw_input("Altura de la piramide: "))
vol = volumen_piramide(A, H)
print "El volumen de la piramide es ", vol
