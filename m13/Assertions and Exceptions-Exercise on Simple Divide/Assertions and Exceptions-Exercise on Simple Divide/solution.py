'''define the simple_divide function here'''
def simple_divide(item, denom):
    '''returns result'''
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
def fancy_divide(list_of_numbers, index):
    '''takes list,denom from main'''
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]
def main():
    '''returns result list when divide with denom'''
    data = input()
    list1 = data.split()
    list2 = []
    for jval in list1:
        list2.append(float(jval))
    single = input()
    index = int(single)
    print(fancy_divide(list2, index))
if __name__ == "__main__":
    main()
