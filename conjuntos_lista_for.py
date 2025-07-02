"""
Dada una lista de nombres, crea un conjunto con los nombres únicos. Luego, crea un
diccionario que cuente cuántas veces aparece cada letra en todos los nombres del
conjunto.
Lista inicial:
nombres = ["Ana", "Luis", "Juan", "Luis", "Ana", "Carlos"]
Impresión esperada en pantalla:
Conjunto de nombres únicos: {'Ana', 'Juan', 'Carlos', 'Luis'}
Conteo de letras:
{'A': 2, 'n': 2, 'a': 3, 'J': 1, 'u': 2, 'C': 1, 'r': 1, 'l': 2, 'o': 1, 's': 2, 'L': 1}

"""
nombres = ["Ana", "Luis", "Juan", "Luis", "Ana", "Carlos"]

no_repetido = set(nombres)
print(no_repetido)
print()
contador = {}

for nombre in no_repetido:
    for letra in nombre:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

print(contador)
