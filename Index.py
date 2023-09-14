# Proyecto de Conceptos Avanzados de programacion
# Jonathan Gandara Salazar
# Carlos Arguello Maladonado

# Agreguen aqui sus nombres como comentario

def main():
    opcion = ""
    while opcion != "3":
        print("Menú:")
        print("1. Calcular fórmula general")
        print("2. Otra opción")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        
        if opcion == "1":
            from formulaGeneral.formula_general import resolver_ecuacion_cuadratica
        elif opcion == "2":
            # Agrega aquí la lógica para la opción 2
            pass
        elif opcion == "3":
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
        print()  # Agrega una línea en blanco después de cada opción seleccionada

if __name__ == "__main__":
    main()
