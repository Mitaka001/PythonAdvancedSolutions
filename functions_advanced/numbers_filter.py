def even_odd_filter(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if key == "even":
            even_nums = [num for num in value if num % 2 == 0]
            new_dict[key] = even_nums
        elif key == "odd":
            odd_nums = [num for num in value if num % 2 != 0]
            new_dict[key] = odd_nums

    return new_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
