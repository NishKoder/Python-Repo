# create fn to return dictionary with cude values 
def cube_dic(n):
    dic = {}
    for i in range(1,n+1):
        dic[i] = i*i*i
    return dic
print(cube_dic(3))


# word counter
def word_count(s):
    count_dic = {}
    for i in s:
        count_dic[i] = s.count(i)
    return count_dic
print(word_count("nishant"))

# insert value from user 
dica = {}
name = input("enter name: ")
age = int(input("enter age: "))
fav_movie = input("enter movies name seprated by ,: ").split(",")
dica["name"] = name
dica["age"] = age
dica["fav_movie"] = fav_movie
print(dica)
for key,value in dica.items():
    print(f"{key} - {value}")


