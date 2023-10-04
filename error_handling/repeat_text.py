# text = input()
# times_to_repeat = input()
# result = ""
#
# if times_to_repeat.isdigit():
#     result += text * int(times_to_repeat)
# else:
#     print("Variable times must be an integer")
#
# print(result)

text = input()

try:
    times = int(input())

except ValueError:
    print("Variable times must be an integer")

else:
    print(text*times)
