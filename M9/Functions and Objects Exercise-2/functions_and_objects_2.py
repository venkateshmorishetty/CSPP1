'''Exercise : Function and Objects Exercise-2'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
def inc(list1):
    '''increase each value'''
    return list1+1
def apply_to_each(list2, fun):
    '''returns list2 '''
    print(list(map(fun, list2)))
def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, inc)
if __name__ == "__main__":
    main()
