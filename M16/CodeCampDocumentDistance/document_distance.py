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
    string2 = dict2.lower().strip().split( )
    string1 = dict1.lower().strip().split( )
    #new1 = re.sub('[^A-Z ]', '', string1).strip()
    #new2 = re.sub('[^A-Z ]', '', string2).strip()
    # print(string1)

    stopword = load_stopwords("stopwords.txt")
    # stop=[]
    # for k in stopword:
    #     stop.append(k)
    list3=[]    
    for i in string1:
        if i not in stopword:
            list3.append(i)
    #print("result",list3)
    list4=[]
    for i in string2:
        if i not in stopword:
            list4.append(i)
    #print(list4)
    dictionary1={}
    c1=0
    c2=0
    for i in list3:
        if i in list4:
            dictionary1[i]=[c1+1,c2+1]
        else:
            dictionary1[i]=[c1+1,c2]
    for i in list4:
        if i in list3:
            dictionary1[i]=[c1+1,c2+1]
        else:
            dictionary1[i]=[c1+0,c2+1]            
    #print(sorted(dictionary1))       
    Numerator=0  
    for i in dictionary1:
        Numerator=Numerator+int(dictionary1[i][0])*int(dictionary1[i][1])
    #print(Numerator) 
    Denominator1=0
    Denominator2=0
    for i in dictionary1:
        Denominator1=Denominator1+dictionary1[i][0]**2
    for i in dictionary1:
        Denominator2=Denominator2+dictionary1[i][1]**2 
    denom=math.sqrt(Denominator1)*math.sqrt(Denominator2)
    #print(denom) 
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
