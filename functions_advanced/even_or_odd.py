# def even_odd(*args, command):
#    command = args[-1]
#    numbers = args[:-1]
#     if command == "even":
#         even_nums = []
#         for num in args:
#             if num % 2 == 0:
#                 even_nums.append(num)
#             else:
#                 continue
#         return even_nums
#
#     if command == "odd":
#         odd_nums = []
#         for num in args:
#             if num % 2 != 0:
#                 odd_nums.append(num)
#             else:
#                 continue
#         return odd_nums
def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]

    if command == "even":
        return [num for num in numbers if num % 2 == 0]
    elif command == "odd":
        return [num for num in numbers if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
