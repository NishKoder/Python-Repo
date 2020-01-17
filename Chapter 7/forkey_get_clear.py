#fromkey - set same value on multiple key
# d = {'name': 'unknown','age':'unknown'}

dic = dict.fromkeys(["name","age","aged"],"unknown")
print(dic)

#get method
print(dic.get("nadme","Not Found"))


d = dic.copy() # have save on diff  memory
d = dic # refer to same dic memory

