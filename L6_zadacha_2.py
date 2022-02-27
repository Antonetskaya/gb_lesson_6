"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""

class Road:
    __length = None
    __width = None
    massa_1m = None
    tolshina = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def intake(self):
        self.massa_1m = 25
        self.tolshina = 0.05
        massa_obsh = self.length * self.width * self.massa_1m * self.tolshina / 1000
        print(f'{massa_obsh} тонн асфальта необходимо')

road_to_village = Road(20000, 6)
road_to_village.intake()