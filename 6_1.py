# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
# метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
# усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.


class TrafficLight:
    def __init__(self, color):
        self._color = color
        self.running()

    def running(self):
        import time
        if self._color == 'green':
            print(self._color)
            time.sleep(3)
            print('yellow')
            time.sleep(2)
            print('red')
            time.sleep(7)
        if self._color == 'yellow':
            print(self._color)
            time.sleep(2)
            print('red')
            time.sleep(7)
            print('green')
            time.sleep(3)
        if self._color == 'red':
            print(self._color)
            time.sleep(7)
            print('green')
            time.sleep(3)
            print('yellow')
            time.sleep(2)


my_color = TrafficLight(input('Введиде цвет светофора (green/red/yellow): '))

