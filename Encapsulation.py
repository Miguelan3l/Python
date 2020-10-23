class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

montecarlo = Car(200, 'cherry red')
impala = Car(250, 'candy blue')
cadillac = Car(300, 'midnight black')

montecarlo.set_speed(300)
montecarlo.__speed = 400
print(montecarlo.get_speed())
print(montecarlo.color)
