'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file

import re
adic = {}
new1 = []
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    n = text.lower()
    m = n.split(" ")
    k = []
    for i in m:
        k.append(re.sub('[^a-z/ ]', '', i).strip())
    return k
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    stop = load_stopwords("stopwords.txt")
    m = []
    for j in docs:
        v = word_list(j)
        m.append(v)
    new1 = []
    new2 = []
    for i in m:
        for j in i:
            if j not in stop:
                new1.append(j)
        new2.append(new1)
        new1 = []
    # c1 = 1 
    # c = 1
    for j in new2:
        c1 = new2.index(j)
        for i in set(j):
            if i not in adic:
                adic[i] = [(c1, j.count(i))]
            else:
                # adic[i][0].append(c1)
                adic[i].append((c1, j.count(i)))
        c1 = 0
    return adic
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
