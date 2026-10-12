import os

def solicitar_notas():
    """Solicita la cantidad de notas y cada una de las calificaciones al usuario."""
    while True:
        try:
            cantidad = int(input("¿Cuántas notas deseas ingresar?: "))
            if cantidad <= 0:
                print("Por favor, ingresa un número mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: Ingresa un número entero válido.")

    notas = []
    for i in range(1, cantidad + 1):
        while True:
            try:
                nota = float(input(f"Ingresa la nota #{i}: "))
                if 0 <= nota <= 100:  
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Ingresa un número válido para la nota.")
                
    return notas


def guardar_en_txt(nombre_archivo, notas, promedio, nota_mayor, nota_menor):
    """Guarda las notas y los resultados calculados en un archivo de texto."""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("=== REPORTE DE NOTAS DEL ESTUDIANTE ===\n\n")
            archivo.write("Notas ingresadas:\n")
            for idx, nota in enumerate(notas, 1):
                archivo.write(f"  - Nota {idx}: {nota:.2f}\n")
            
            archivo.write("\n=== RESUMEN ===\n")
            archivo.write(f"Promedio general: {promedio:.2f}\n")
            archivo.write(f"Nota mayor: {nota_mayor:.2f}\n")
            archivo.write(f"Nota menor: {nota_menor:.2f}\n")
            
        print(f"\n¡Éxito! Los datos han sido guardados en '{nombre_archivo}'.")
    except IOError as e:
        print(f"Error al intentar guardar el archivo: {e}")


def main():
    print("--- REPORTE DE NOTAS ---\n")
    

    notas = solicitar_notas()
    
  
    promedio = sum(notas) / len(notas)
    nota_mayor = max(notas)
    nota_menor = min(notas)
    

    print("\n" + "=" * 35)
    print("RESUMEN DE RESULTADOS")
    print("=" * 35)
    print(f"Promedio:    {promedio:.2f}")
    print(f"Nota Mayor:  {nota_mayor:.2f}")
    print(f"Nota Menor:  {nota_menor:.2f}")
    
 
    nombre_txt = "notas_estudiante.txt"
    guardar_en_txt(nombre_txt, notas, promedio, nota_mayor, nota_menor)


if __name__ == "__main__":
    main()