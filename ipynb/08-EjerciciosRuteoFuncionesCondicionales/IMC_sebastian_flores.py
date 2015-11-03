def imc(p,a):
    a_m = a/100
    i = float(p)/a**2
    print "Su imc es", i, "lo que esta",  
    if i<10:
        print "Muy bajo!"
    if i>30:
        print "Muy alto!"
    else:
        print "Bien"
    return

imc(75, 175)
imc(40, 160)
imc(200, 200)

# Input de usuario
peso_kg = float(raw_input("Ingrese peso [kg]:"))
altura_cm = float(raw_input("Ingrese altura [cm]:"))

imc(peso_kg, altura_cm)

