from control import ControlParque


def prueba():
    control = ControlParque()

    individuo = control.registrar_individuo("12345", "Calvin Clein", 18)
    print("Debe salir: $40000")
    print("Valor: $", control.calcular_precio_individuo(individuo))

    grupo = control.registrar_grupo("La empresita", 2)
    print("Debe salir: $76000")
    print("Valor: $", control.calcular_precio_grupo(grupo))


if __name__ == "__main__":
    prueba()
