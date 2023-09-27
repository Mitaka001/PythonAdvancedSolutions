n, m = input().split()
first_set = set()
second_set = set()

for _ in range(int(n)):
    first_set.add(input())

for _ in range(int(m)):
    second_set.add(input())

result = first_set & second_set
print("\n".join(result))
