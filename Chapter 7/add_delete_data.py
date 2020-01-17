user = {
    "name": "nameee",
    "age": 23,
    "fav_movie": ["coco", "moko"],
    "fav_tunes": ["dodo", "kopo"],
    
}


# add data

user["fav_song"] = ["s1","s2"]
print(user)


#pop method
user.pop('fav_tunes') # also return pop value
print(user)

#pop item method - radomly remove anyone of user - return type tuple
print(user.popitem())

#update method
more_info = {"he":12,"he2":12}
user.update(more_info)
print(user)

