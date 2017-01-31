class TestOfStaticAndClassMethods:

    X = 5
    Y = 10

    def __init__(self):
        self.value = 'value'

    def instance_method(self):
        print('inside instance method: ', self.value)

    @classmethod
    def class_method(cls):
        print('class method -> X: {}, Y: {}'
              .format(cls.X, cls.Y))

    @staticmethod
    def static_method_wrong_using():
        print('static method wrong using -> X: {}, Y: {}'
            .format(TestOfStaticAndClassMethods.X,
                    TestOfStaticAndClassMethods.Y))

    @staticmethod
    def static_method_correct_using(x, y):
        print('static method CORRECT using -> X: {}, Y: {}'
              .format(x, y))

