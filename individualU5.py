import re

path ="u5.txt"

try:
    archivo= open(path, 'r')
except:
    print ("el archivo no existe")
    quit()

texto= ""

for linea in archivo:
    texto += linea


print (texto)
print ("________________________________________________________________________________")



senten = r'([a-z0-9]+\s*=\s*[a-z0-9+]+)'
sentenR = re.findall(senten,texto)
print ("\nESTAS SON LAS SENTECIAS DE AIGNACION\n"), sentenR
print ("________________________________________________________________________________")

print("\n")
opera = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'
operaR = re.findall(opera,texto)
print ("\nESTAS SON LAS OPERACIONES ENCONTRADAS\n"), operaR
print("\n")
print ("________________________________________________________________________________")

print("\n")

boole = r"([A-Za-z0-9|a-z0-9]+\s*[=|<|>|!|<=|>=]+\s*[A-Za-z0-9|a-z0-9]+)"
booleaR = re.findall(boole, texto)
print ("BOOLEANOS ENCONTRADOS\n"), booleaR
print("\n")
print ("________________________________________________________________________________")

print("\n")
pfor= r'(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)'
pwhile= r'(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
pif = r'(if+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
ptry = r'(try:+\s*[A-Za-z0-9-_]+\s*except+\s*[A-Za-z0-9-_]+\s*:)'

pforR = re.findall(pfor, texto)
print ("FOR ENCONTRADOS:\n"), pforR

pwhileR = re.findall(pwhile,texto)
print ("WHILE EN.CONTRADS:\n"), pwhileR

pifR = re.findall(pif,texto)
print ("IF ENCONTRADOS:\n"), pifR

ptryR = re.findall(ptry,texto)
print ("TRY ENCONTRADOS:\n"), ptryR

print("\n")
print ("________________________________________________________________________________")

print("\n")
formucompeja= r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
formucompejaR = re.findall(formucompeja,texto)
print ("FORMULAS COMPLEJAS:\n"), formucompejaR
print("\n")
print ("________________________________________________________________________________")



