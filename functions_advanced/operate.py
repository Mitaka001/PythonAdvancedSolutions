from functools import reduce


def operate(operator, *args):
    def add():
        return reduce(lambda a, b: a+b, args)

    def subtract():
        return reduce(lambda a, b: a-b, args)

    def multiply():
        return reduce(lambda a, b: a*b, args)

    def divide():
        return reduce(lambda a, b: a/b, args)

    if operator == "+":
        return add()

    elif operator == "-":
        return subtract()

    elif operator == "*":
        return multiply()

    elif operator == "/":
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

# Vtori nachin za reshavane
# from functools import reduce
# def operate(sign, *args):
#     return reduce(lambda a, b: eval(f"{a}{sign}{b}"), args)
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
