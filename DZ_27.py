# Задание 1
# Создайте реализацию паттерна Command. Протестируйте работу созданного класса.
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class Light:
    def turn_on(self):
        print('Свет включен')

    def turn_off(self):
        print('Свет выключен')


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()
remote.set_command(light_off)
remote.press_button()

# Задание 2
# Есть класс, предоставляющий доступ к набору чисел. Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и выполнять набор операций над ними (сумма,
# максимум, минимум и т.д.). При каждой попытке доступа к этому набору необходимо вносить запись в
# лог-файл. При реализации используйте паттерн Proxy (для логгирования) и другие необходимые паттерны.
import logging


class Numbers:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def update_data(self):
        self.data = []
        with open(self.filename, 'r') as file:
            for line in file:
                num = int(line)
                self.data.append(num)
        return self.data

    def get_sum(self):
        self.update_data()
        return sum(self.data)

    def get_max(self):
        self.update_data()
        return max(self.data)

    def get_min(self):
        self.update_data()
        return min(self.data)


class NumbersProxy:
    def __init__(self, filename):
        self.numbers = Numbers(filename)
        self.logger = logging.getLogger('NumbersProxy')

    def update_data(self):
        self.numbers.update_data()
        self.logger.info('Data updated')

    def get_sum(self):
        result = self.numbers.get_sum()
        self.logger.info(f'Sum: {result}')
        return result

    def get_max(self):
        result = self.numbers.get_max()
        self.logger.info(f'Max: {result}')
        return result

    def get_min(self):
        result = self.numbers.get_min()
        self.logger.info(f'Min: {result}')
        return result


filename = 'data.txt'
proxy = NumbersProxy(filename)
proxy.update_data()
print(proxy.get_sum())
print(proxy.get_max())
print(proxy.get_min())

# Задание 3
# Создайте приложение для работы в библиотеке. Оно должно оперировать следующими сущностями: Книга,
# Библиотекарь, Читатель. Приложение должно позволять вводить, удалять, изменять, сохранять вфайл,
# загружать из файла, логгировать действия, искать информацию (результаты поиска выводятся на экран
# или файл) о сущностях. При реализации используйте максимально возможное количество паттернов
# проектирования.