class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        try:
            float(self.a)
            float(self.b)
        except ValueError:
            return 'переменные могут быть только числового типа(int, float)'
        else:
            return float(self.a) + float(self.b)

    def sub(self):
        try:
            float(self.a)
            float(self.b)
        except ValueError:
            return 'переменные могут быть только числового типа(int, float)'
        else:
            return float(self.a) - float(self.b)

    def div(self):
        try:
            float(self.a)
            float(self.b)
        except ValueError:
            return 'переменные могут быть только числового типа(int, float)'
        else:
            try:  # проверка деления на ноль
                1 / float(self.b)
            except ZeroDivisionError:
                return 'Деление на ноль! Аргумент b не может быть равен нулю!'
            else:
                return float(self.a) / float(self.b)

    def mul(self):
        try:
            float(self.a)
            float(self.b)
        except ValueError:
            return 'переменные могут быть только числового типа(int, float)'
        else:
            return float(self.a) * float(self.b)


if __name__ == "__main__":
    print(Calculator(2.1, 9).sum())
    print(Calculator(5, 9).sub())
    print(Calculator(5, 9).div())
    print(Calculator(2.6, 9).mul())
    print(float(2))
    print(Calculator(5, 'df'))