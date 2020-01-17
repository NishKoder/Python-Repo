# Dictonary - unordered collection of data key : value pair
# Syntax:
# dict_name = {kay:value,key:value}
# second Way to create Dict
dic_user = dict(age=12, name="sdsd")
print(dic_user["age"])  # access dic data


user = {
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
print(user["sons"]["name"])

# add data in blank dic
users = {}
users["name"] = "nish"
print(users)
