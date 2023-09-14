import math
from termcolor import colored
import os
os.system("color")
# def funcion1 (x1, x2):

import math

def resolver_ecuacion_cuadratica():
    valor1 = int(input("Ingrese el primer termino del binomio (el coeficiente de la x > 1)"))
    valor2 = int(input("Ingrese el segundo termino del binomio (el segundo)"))
    res1 = pow(valor1, 2)  # se calcula la potencia el primer valor del binomio
    res2 = (2*valor2)  # se calcula el segundo valor del binomio
    res3 = pow(valor2, 2)  # se calcula la potencia el segundo valor del binomio
    print("La solución del binomio es: ", res1, "x^2 +", res2, "x +", res3)  # se muestra la solución
    resultadox1 = -((res2)+(math.sqrt((pow(res2, 2))-(4)*(res1)*(res3))))/2*(res1)
    print("El resultado de x1 = ", resultadox1)
    resultadox2 = -((res2)-(math.sqrt((pow(res2, 2))-(4)*(res1)*(res3))))/2*(res1)
    print("El resultado de x2 = ", resultadox2)

resolver_ecuacion_cuadratica()