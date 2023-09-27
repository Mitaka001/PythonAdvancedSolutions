n = int(input())
compounds = set()

for _ in range(n):
    chemical_compounds = input().split()

    for compound in chemical_compounds:
        compounds.add(compound)

for element in compounds:
    print(element)
