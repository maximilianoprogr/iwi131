def imc(peso, altura):
    peso_en_kg = float(peso)
    altura_en_m = float(altura) / 100.0
    IMC = peso_en_kg/altura_en_m**2
    print "Su IMC es", IMC
    return
