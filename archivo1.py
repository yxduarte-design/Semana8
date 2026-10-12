#Leer un archivo llamado archivo1.py
archivo = open("datos.txt", "r", encoding="utf-8") #para identificar las letras en espanol y acentos
print(archivo.read())
archivo.close()