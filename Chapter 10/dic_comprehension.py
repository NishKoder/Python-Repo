# square = {1:1,2:4,3:9}
def square_dict():
    return {f"Square of {num} is ":num**2 for num in range(1,11) }
print(square_dict())


# word count
def count_charater(dic):
    return{key:value.count("h") for key,value in dic.items() if type(value) == str}
print(count_charater({'name':"hfgdbhhdfdh",'nn':"12",'sd':2323}))

# dic if else - show key is even or odd with value
def dic_ifelse(num):
    return {key:("Even" if key%2 == 0 else "Odd") for key in range(1,num)}
print(dic_ifelse(13))