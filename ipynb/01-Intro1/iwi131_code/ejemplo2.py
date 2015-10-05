anexos = {'Cesar': 4001, 'Sebastian': 4002}
anexos['Claudio'] = 4003
print anexos

print anexos['Sebastian']

del anexos['Claudio']
anexos['Patricio'] = 4004

print anexos

if "Claudio" in anexos:
    print anexos["claudio"]

if "claudio" in anexos:
    print anexos["claudio"]
