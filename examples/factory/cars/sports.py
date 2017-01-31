from examples.factory.cars.abstract import AbstractCar


class SportCar(AbstractCar):

    TYPE = 'SPORT CAR'

    def __str__(self):
        return '{} {}'.format(super().__str__(), 'sport')
