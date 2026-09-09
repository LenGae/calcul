a = int(input("Число: "))
b = int(input("Число 2: "))
op = input("Знак: ")

class Calculator:
    def umn(self, a, b):
        return a*b


calculator = Calculator()

if op == "*":
    res = calculator.umn(a, b)

print(res)