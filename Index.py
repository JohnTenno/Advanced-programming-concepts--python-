from primer_funcion import funcion_1
from funciones.segunda_funcion import funcion_2
from funciones.tercera_funcion import funcion_3

def main():
    while True:
        try:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
            c = float(input("Ingrese el valor de c: "))

            resultado = funcion_1(a, b, c)
            x1 = funcion_2(a, b, resultado)
            x2 = funcion_3(a, b, resultado)


            print("El valor del discriminante es:", resultado)
            print("El valor de x1 es:", x1)
            print("El valor de x2 es:", x2)
            break
        except ValueError as error:
            print("Error:", error)
            print("Por favor, ingrese valores válidos para a, b y c.")

if __name__ == "__main__":
    main()

