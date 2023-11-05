class Numerator:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def func(self):
        if self.__num1 <= 3:
            self.__num1 += 11
        elif self.__num1 >= 3:
            self.__num1 -= 2

        if self.__num2 <= 8:
            self.__num2 += 9
        elif self.__num2 >= 8:
            self.__num2 -= 4
        print(self.__num1 + self.__num2)


num11 = Numerator(3, 8)
num11.func()

num1 = 3
num2 = 8