def positive_and_negative(numbers):
    negative = []
    positive = []

    for number in numbers:
        num = int(number)
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)

    def strongest_numbers():
        if abs(sum(negative)) > sum(positive):
            return "The negatives are stronger than the positives"
        if abs(sum(negative)) < sum(positive):
            return "The positives are stronger than the negatives"

    return f"{sum(negative)}\n{sum(positive)}\n{strongest_numbers()}"


nums = input().split()
result = positive_and_negative(nums)
print(result)
