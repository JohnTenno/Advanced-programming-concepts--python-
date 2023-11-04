import os
from termcolor import colored

# diccionarios globales
Materias = {
    "CB370": "CÁLCULO VECTORIAL",
    "CB371": "ÁLGEBRA LINEAL",
    "CB372": "MATE DISCRETAS AVAZADAS",
    "CB373": "ECU DIFERENCIALES",
    "CI374": "ANÁLISIS DE ALGORITMOS",
    "I301": "INGLÉS 3"
}

# lista de la semana
dias_semana = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES"]

# Se rea un horario vacio con los dias de la semana
# con un rango de horas limitado de 7 a 14 horas
horario = {
    dia: {hora: None for hora in range(7, 14)}
    for dia in dias_semana
}

# Esto crea un diccionario para poder rastraer un error o una restriccion
# haciendo que quede asi
# {
#     "CÁLCULO VECTORIAL": 0,
#     "ÁLGEBRA LINEAL": 0
# }
horas_asignadas_por_materia = {materia: 0 for materia in Materias}


# y este asi
# {
#     "CÁLCULO VECTORIAL": {
#         "Lunes": 0,
#         "Martes": 0,
#         "Miercoles": 0
#     },
#     "ÁLGEBRA LINEAL": {
#         "Lunes": 0,
#         "Martes": 0,
#         "Miercoles": 0
#     }
# }
# asi podemos saber cuantas veces a sido registrada una materia por dia y cuantas horas tiene ya a a la semana

horas_asignadas_por_materia_por_dia = {
    materia: {dia: 0 for dia in dias_semana} for materia in Materias}


def asignar_materia(dia, hora, cve_materia):
    try:
        if hora < 7 or hora > 13:
            raise ValueError(
                "Error: La hora debe ser del turno matutino."
            )
        if horas_asignadas_por_materia[cve_materia] >= 5:
            raise ValueError(
                "Error: La materia ha alcanzado el limite de 5 horas asignadas por semana."
            )

        if horas_asignadas_por_materia_por_dia[cve_materia][dia] >= 2:
            raise ValueError(
                "Error: La materia ha alcanzado el limite de 2 horas asignadas en este dia."
            )

        if horario[dia][hora] is not None:
            raise ValueError(
                "Error: La hora ya está ocupada por otra materia."
            )

        # Si no hay errores, se asigna la materia
        horario[dia][hora] = cve_materia
        horas_asignadas_por_materia[cve_materia] += 1
        horas_asignadas_por_materia_por_dia[cve_materia][dia] += 1
    except ValueError as error:
        print(error)


def imprimir_horario(dia):
    print(f"\nHorario de {dias_semana[dia - 1]}")
    print("HORA    | MATERIA")
    print("-" * 20)
    for hora, materia in horario[dias_semana[dia - 1]].items():
        print(f"{hora:2d}-" f"{hora + 1:2d} | {materia if materia else 'Libre'}")
    print()


def guardar_horario_en_archivo():
    with open("horario.txt", "w") as file:
        file.write("Mi horario\n")
        file.write("-" * 70 + "\n")
        file.write(
            "   HORA    | LUNES     MARTES     MIERCOLES   JUEVES    VIERNES\n")
        file.write("-" * 70 + "\n")
        for hora in range(7, 14):
            file.write(f"{hora:2d}-{hora + 1:2d}  |")
            for dia in dias_semana:
                materia = horario[dia][hora]
                file.write(f" {materia if materia else 'Libre':<9} |")
            file.write("\n")
        file.write("-" * 70 + "\n")


def main():
    while True:
        print("\nOpciones:")
        print("1: Ingresar Materia")
        print("2: Imprimir un dia del horario")
        print("3: Imprimir Horario en archivo")
        print("4: Salir")

        try:
            opcion = int(input("¿Opción?: "))

            if opcion == 1:
                print("Ingresar Materia")
                # Este bucle for recorre a por el
                # diccionario de materias para mostrar las claves y
                # nombres de las materias disponibles en el horario.
                for clave, materia in Materias.items():
                    print(f"{clave}: {materia}")

                cve_materia = input("¿Clave?: ")
                if cve_materia not in Materias:
                    print("Clave no encontrada")
                else:
                    hora = int(input("¿Hora? (7 a 13 hrs): "))

                    print("Dias de la semana:")
                    for i, dia in enumerate(dias_semana):
                        print(f"{i + 1}: {dia}")
                    dia = int(input("¿Dia?: "))

                    asignar_materia(dias_semana[dia - 1], hora, cve_materia)

            elif opcion == 2:
                dia = int(input("¿Dia a imprimir?: "))
                imprimir_horario(dia)

            elif opcion == 3:
                print("Horario a un archivo")
                guardar_horario_en_archivo()
                print("Archivo listo")

            elif opcion == 4:
                break

        except ValueError:
            print(colored("Opcion no vlida", "red"))

    print("¡Adiós!")


if __name__ == "__main__":
    main()
