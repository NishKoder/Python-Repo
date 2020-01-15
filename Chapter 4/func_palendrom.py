def palindrom(name):
    rev = name[::-1]
    if name == rev:
        return True
    return False


print(palindrom("1211"))
