a = int(input("Число: "))
b = int(input("Число 2: "))
op = input("Знак: ")

class Calculator:
    def plus(self, a, b):
        return a+b

calculator = Calculator()

if op == "+":
    res = calculator.plus(a, b)

print(res)