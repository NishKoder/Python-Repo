user_info = {
    "name": "nameee",
    "age": 23,
    "fav_movie": ["coco", "moko"],
    "fav_tunes": ["dodo", "kopo"],
    "sons": {
        "name": "nameee",
        "age": 23,
        "fav_movie": ["coco", "moko"],
        "fav_tunes": ["dodo", "kopo"],
    },
}


# check if key exist in dictionory
if "name" in user_info:
    print("Present")

# check if value exist in dict
if 23 in user_info.values():
    print("Present")



usr_info_value = user_info.values()
print(type(usr_info_value))


# loop dict
for i in user_info:
    print(user_info[i])

#item method - send tuple with key as first and value as second
print("Itme Method")
for i in user_info.items():
    print(i)


print("Itme Method Second")
for key,value in user_info.items():
    print(f"{key} - {value}")

