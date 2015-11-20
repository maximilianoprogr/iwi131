import mi_modulo

n = int(raw_input("Numero de lados: "))
a = float(raw_input("Arista del poligono: "))
area = mi_modulo.area_poligono(n, a)
print "El area del poligono es", area
