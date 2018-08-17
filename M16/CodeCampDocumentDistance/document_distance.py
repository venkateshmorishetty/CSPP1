'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    string2 = dict2.lower()
    string1 = dict1.lower()
    new1 = string1.strip().split(" ")
    new2 = string2.strip().split(" ")
    new3 = []
    new4 = []
    stopword = load_stopwords("stopwords.txt")
    for word in new1:
        i = re.sub('[r,^a-z\ ]', '', word)
        new3.append(i)
    for word in new2:
        i = re.sub('[r,^a-z\ ]', '', word)
        new4.append(i)
    list3 = []
    list4 = []
    for i in new3:
        val = len(i)
        if i not in stopword and val > 0:
            list3.append(i)
    for i in new4:
        val = len(i)
        if i not in stopword and val > 0:
            list4.append(i)
    dictionary1 = {}
    dictionary2 = {}
    for i in list3:
        if i in dictionary1:
            dictionary1[i] += 1
        else:
            dictionary1[i] = 1
    for i in list4:
        if i in dictionary2:
            dictionary2[i] += 1
        else:
            dictionary2[i] = 1
    numerator = 0
    for i in dictionary1:
        if i in dictionary2:
            numerator = numerator + (dictionary1[i]*dictionary2[i])
    denominator1 = 0
    denominator2 = 0
    for i in dictionary1:
        denominator1 = denominator1 + (dictionary1[i])**2
    for i in dictionary2:
        denominator2 = denominator2 + (dictionary2[i])**2
    denom = (math.sqrt(denominator1))*(math.sqrt(denominator2))
    return numerator / denom
def load_stopwords(_):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(_, 'r') as _:
        for line in _:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))
if __name__ == '__main__':
    main()
