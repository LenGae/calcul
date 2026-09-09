a = int(input("Число: "))
b = int(input("Число 2: "))
op = input("Знак: ")

class Calculator:
    def pod(self, a, b):
        if b == 0:
            return "На ноль нельзя делить"
        return a/b

calculator = Calculator()

if op == "/":
    res = calculator.pod(a, b)

print(res)