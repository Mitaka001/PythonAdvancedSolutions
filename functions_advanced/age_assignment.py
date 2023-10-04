def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            result.append(f"{name} is {kwargs[first_letter]} years old.")

    sorted_result = sorted(result)
    return '\n'.join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
