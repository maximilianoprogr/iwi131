# Inicializacion
cantidad_notas = 0
suma_notas = 0
peor_alumno = ""
peor_rol = ""
peor_nota = 101
mejor_alumno = ""
mejor_rol = ""
mejor_nota = -1

seguir_ciclo = True
while seguir_ciclo:
    alumno = raw_input("Nombre del alumno :")
    if alumno == "STOP":
        break
    rol = raw_input("Rol del alumno :")
    if rol == "STOP":
        break
    nota = raw_input("Nota del alumno :")
    if nota == "STOP":
        break
    else:
        nota = float(nota)
    # Si llegamos aqui, alumno, rol y nota estan bien definidos
    # Actualizar cantidad de notas
    cantidad_notas += 1
    # Actualizar suma de notas
    suma_notas += nota
    # Actualizar peor alumno
    if nota < peor_nota:
        peor_alumno = alumno
        peor_rol = rol
        peor_nota = nota
    # Actualizar peor alumno
    if nota > mejor_nota:
        mejor_alumno = alumno
        mejor_rol = rol
        mejor_nota = nota

# Imprimir resultado
print ""
print "RESULTADOS:"
print "Se ingresaron", cantidad_notas, "alumnos"
print "El promedio de notas es ", suma_notas/cantidad_notas
print "El peor alumno es", peor_alumno, peor_rol, "con nota", peor_nota
print "El mejor alumno es", mejor_alumno, mejor_rol, "con nota", mejor_nota
