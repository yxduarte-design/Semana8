listas = [1, 2, 3, 4, 5 ,6, 2, 0, 1, 2, 1, "hola"]
#print(listas)

conjuntos = {1, 2, 3, 4, 5 ,6, 2, 0, 1, 2, 1, "hola"}
#print(conjuntos)

tuplas = (1, 2, 3, 4, 5 ,6, 2, 0, 1, 2, "hola")
#print(tuplas)

diccionarios = {"Estudiante": "Juanito"}



nuevalista= []
nuevalista.append(listas)
nuevalista.append(conjuntos)
nuevalista.append(tuplas)
nuevalista.append(diccionarios)
print(nuevalista)

for item in nuevalista:
    print(item)

"""for item in nuevalista:
    print(type(nuevalista))
"""



with open("texto.txt","+w", encoding="utf-8") as archivo:
    for item in nuevalista:
        archivo.write(str(item)+ "\n")