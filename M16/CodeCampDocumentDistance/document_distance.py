'''
    Document Distance - A detailed description is given in the PDF
'''
import math,re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    string1 = ''
    string2 = ''
    #string1 = dict1.lower()
    string2 = dict2.lower()
    string1 = dict1.lower()
    new1 = string1.strip().split(" ")
    new2 = string2.strip().split(" ")
    new3=[]
    new4=[]
    stopword = load_stopwords("stopwords.txt")
    for word in new1:
        i=re.sub('[^a-z\ ]', '',word)
        new3.append(i)
    for word in new2:
        i=re.sub('[^a-z\ ]', '',word)
        new4.append(i)
    list3=[] 
    list4=[]   
    for i in new3:
        if i not in stopword and len(i)>0:
            list3.append(i)
    for i in new4:
        if i not in stopword and len(i)>0:
            list4.append(i)
    dictionary1={}
    dictionary2={}
    for i in list3:
        if i in dictionary1:
            dictionary1[i]+=1
        else:
            dictionary1[i]=1 
    for i in list4:
        if i in dictionary2:
            dictionary2[i]+=1
        else:
            dictionary2[i]=1                     
    Numerator=0  
    for i in dictionary1:
        if i in dictionary2:
            Numerator=Numerator+(dictionary1[i]*dictionary2[i])
    Denominator1=0
    Denominator2=0
    for i in dictionary1:
        Denominator1=Denominator1+(dictionary1[i])**2
    for i in dictionary2:
        Denominator2=Denominator2+(dictionary2[i])**2 
    denom=(math.sqrt(Denominator1))*(math.sqrt(Denominator2)) 
    return Numerator/denom
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
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
