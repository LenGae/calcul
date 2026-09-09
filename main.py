a = int(input("Число: "))
b = int(input("Число 2: "))
op = input("Знак: ")

class Calculator:
    def plus(self, a, b):
        return a+b
    def umn(self, a, b):
        return a*b
    def st(self, a, b):
        return a-b
    def pod(self, a, b):
        if b == 0:
            return "На ноль нельзя делить"
        return a/b

calculator = Calculator()

if op == "+":
    res = calculator.plus(a, b)
elif op == "*":
    res = calculator.umn(a, b)
elif op == "-":
    res = calculator.st(a, b)
elif op == "/":
    res = calculator.pod(a, b)

print(res)