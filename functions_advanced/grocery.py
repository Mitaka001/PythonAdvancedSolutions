def grocery_store(**kwargs):
    sorted_receipt = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    receipt = "\n".join([f"{item[0]}: {item[1]}" for item in sorted_receipt])
    return receipt


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
