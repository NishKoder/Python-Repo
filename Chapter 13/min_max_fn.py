names = ["test", "testin", "testing"]
print(max(names, key=lambda item: len(item)))
print(min(names, key=lambda item: len(item)))

std = {
    "first": {"score": 20, "age": 40},
    "second": {"score": 23, "age": 30},
    "third": {"score": 33, "age": 32},
}

print(max(std, key=lambda item: std[item]["score"]))
# std2 = [
#     {"name": "ee", "score": 20, "age": 40},
#     {"name": "ee2", "score": 10, "age": 20},
#     {"name": "ee3", "score": 23, "age": 42},
# ]

# print(max(std2, key=lambda item: item.get("score")).get("name"))
