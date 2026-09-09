a = int(input("Число: "))
b = int(input("Число 2: "))
op = input("Знак: ")

class Calculator:
    def st(self, a, b):
        return a-b

calculator = Calculator()

if op == "-":
    res = calculator.st(a, b)


print(res)