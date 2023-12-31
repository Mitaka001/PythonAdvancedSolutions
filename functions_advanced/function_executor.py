def func_executor(*args):
    results = ""

    for function, arguments in args:
        result = function(*arguments)
        results += f"{function.__name__} - {result}\n"

    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
