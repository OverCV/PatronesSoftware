from controladoras import ParqueNatural
from entidades import Animal, Planta


def reporte():
    parque = ParqueNatural()

    animal = Animal("Felino", False, 2)
    parque.adicionar_animal(animal)
    animal = Animal("Mamífero", True, 50)
    parque.adicionar_animal(animal)

    planta = Planta("Frutal", "Fuente de vitaminas", 160)
    parque.adicionar_planta(planta)
    planta = Planta("Gramínea", "Alimento para ganado", 20)
    parque.adicionar_planta(planta)

    print('REPORTE CONSOLIDADO')
    print('Días de adaptación: ', parque.promedioDiasAdaptacion())
    print('Total de seres vivos: ', parque.cantidadTotalSeresVivos())


if __name__ == "__main__":
    reporte()
