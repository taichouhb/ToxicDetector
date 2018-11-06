import pdb
from collections import defaultdict

def featurize(input):
    #Takes in Nx (2) array of tuples. 
    
    # Parse input sentence into D features for each sentence  
    data = feats(input)
    
    
    #Perhaps need to take mini-batches, or we can train on the whole thing
    #Split by sampling into three sets train, val, test
    
    
    #Return data_train, data_val, data_test subsets of full data, 
    #data_train being largest, probably  
    return None, None, None

def feats(input):
    #Parse input into features of length D.
    #Pandas DF N x 3 
    globalTable = parseGlobal()
    pdb.set_trace()
    for n, row in input.iterrows():
        idd, comment, index = row
        #Tokenize comment
        newSet = ',.!?\"'
        exclamation = comment.count("!")
        table =  str.maketrans({key:None for key in newSet})
        translated = comment.translate(table)
        tokens = translated.split(" ")
        
    
    #output returns in N x D, N (labels, N of them)
    #Perhaps preprocess the labels here so they are binary class, instead of 10 classes
    return None, None

def parseGlobal():
    directory = 'slurs/'
    fileNames = [('noswear.csv',7), ('disability.csv',13), ('rsd.txt',14)]
    #Index Values [7, 13, 14]
    wordToFeature = defaultdict() #Word -> [Index X]
    counter = 1
    for f,idx in fileNames:
        words = open(directory+f, 'r').read()
        words = words.split(', ')
        for w in words:
            if w not in wordToFeature:
                wordToFeature[w] = set()
            wordToFeature[w].add(idx)
    return wordToFeature



"""
Some thoughts on the features that we will implment:
1. # sexual organs
2. # volient words
3. # family words
4. # negative adj
5. # negative cyber slangs
6. # caps
7. # swears  -- close "fucky"
8. # "!"
9. # complimentart words
10. # simple emoji :) 
11. # xD, :D
12. # \\n
13. Disability
14. Racial Slurs DB

"""