file = open("input.txt", "r")
file = file.read()
file = file.split('\n')
dict_= {}
for element in file:
    k, v = element.split()
    print(k, v)
    v = int(v)
    if k in dict_:
        if v not in dict_[k]:
            dict_[k].append(v)
    else:
        dict_[k] = [v]


print(dict_)
