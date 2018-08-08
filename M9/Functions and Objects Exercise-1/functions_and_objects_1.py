'''Exercise : Function and Objects Exercise-1'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
def apply_to_each(list2, fun):
    '''increase each element to 1'''
    print(list(map(fun, list2)))
def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, abs)
if __name__ == "__main__":
    main()
