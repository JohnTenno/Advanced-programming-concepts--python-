import math

def funcion_1(a, b, c):
    if a == 0:
        raise ValueError("El valor de 'a' no puede ser cero.")
    
    #el discriminante es la parte de la formula general bajo la raiz cuadrada
    discriminante = (b ** 2) - (4 * a * c)
    if discriminante < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    
    return math.sqrt(discriminante)