n = int(raw_input('Ingrese n: '))
es_primo = True
d = 2
while d < n:
    if n % d == 0:
        es_primo = False
    d = d + 1
if es_primo:
    print(n, 'es primo')
else:
    print(n, 'es compuesto')
