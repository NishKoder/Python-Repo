fruits = ["grapes", "mango", "apple"]
# fruits.sort() - not working with tuple
# print(fruits)


fruits2 = ("grapes", "mango", "apple")
# print(sorted(fruits2))


fruits3 = {"grapes", "mango", "apple"}
# print(sorted(fruits3))


guitars = [
    {"model": "model1", "price": 32007},
    {"model": "model2", "price": 32200},
    {"model": "model3", "price": 32060},
    {"model": "model4", "price": 32400},
]

print(sorted(guitars, key=lambda item: item.get("price"), reverse=True))

