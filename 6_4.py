# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево).  А также методы: go, stop, turn(direction), которые
# должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
# и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат

class Cars:
    def __init__(self, color, name, is_police=False, speed=0):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        if self._speed == 0:
            print('Машина остановилась')

    def turn(self, direction):
        if self._speed > 0:
            print(f'Поверните в{direction}')

    def show_speed(self):
        if self._speed > 0:
            print(f'Ваша скорость {self._speed}')

    def show_is_police(self):
        if self._speed > 0 and self._is_police ==True:
            print(f'Внимание, полицейская машина')


class PoliceCar(Cars):
    pass

class SportCar(Cars):
    pass

class TownCar(Cars):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print(f'Пожалуйста, снизьте скорость!')


class WorkCar(Cars):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print(f'Пожалуйста, снизьте скорость!')


one_car = Cars('Зеленая', 'Kia', False, 50)
one_car.go()
one_car.stop()
one_car.turn('лево')
one_car.show_speed()
one_car.turn('право')
print()
two_car = PoliceCar('Синяя', 'Kia', True, 70)
two_car.show_is_police()
two_car.go()
two_car.stop()
two_car.turn('лево')
two_car.show_speed()
two_car.turn('право')
print()
three_car = WorkCar('Белая', 'Kia', True, 80)
three_car.go()
three_car.stop()
three_car.turn('лево')
three_car.show_speed()
three_car.turn('право')
