import pdb
from collections import defaultdict
import numpy as np



def featurize(input, stage='train'):
    #Takes in Nx (2) array of tuples. 
    
    # Parse input sentence into D features for each sentence  
    x, y = feats(input, stage)
    
    
    #Perhaps need to take mini-batches, or we can train on the whole thing
    #Split by sampling into three sets train, val, test
    
    
    #Return data_train, data_val, data_test subsets of full data, 
    #data_train being largest, probably  
    return x, y

def feats(input, stage='train'):
    #Parse input into features of length D.
    #Pandas DF N x 3 
    globalTable, totalFeatures = parseGlobal()
    featureMatrix = []
    labels = []

    for ind, row in input.iterrows():
        featureVector = np.array([0]*totalFeatures)
        idd, comment = row['id'], row['comment_text']
        if stage == 'train':
            label = [row['toxic'], row['severe_toxic'], row['obscene'], \
                 row['threat'], row['insult'], row['identity_hate']]
        #Tokenize comment
        newSet = ',.!?\"'
        exclamation = comment.count("!")
        table =  str.maketrans({key:None for key in newSet})
        translated = comment.lower().translate(table)
        
        tokens = multipleWords(1, translated) # every 1 word
        for t in tokens: 
            if t in globalTable:
                for ind in globalTable[t]:
                    featureVector[ind] += 1
        featureMatrix.append(featureVector)

        doubleTokens = multipleWords(2, translated) # every 2 words
        for t in doubleTokens: 
            if t in globalTable:
                for ind in globalTable[t]:
                    featureVector[ind] += 1
        featureMatrix.append(featureVector)
        
        tripleTokens = multipleWords(3, translated) # every 3 words
        for t in tripleTokens: 
            if t in globalTable:
                for ind in globalTable[t]:
                    featureVector[ind] += 1
        featureMatrix.append(featureVector)

        labels.append(label)

        
    featureMatrix = np.array(featureMatrix)
    if stage=='train':
        labels = np.array(labels)
    else: 
        labels = None
    return featureMatrix, labels

def multipleWords(span, input):
    token = input.split(" ")
    if (span > 1):
        token = [' '.join(token[i:i+span]) for i in range(0,len(token),span)]
    return token
    
        

def parseGlobal():
    directory = 'slurs/'
    fileNames = [('sexual.csv', 1), ('negAdj.csv', 4), ('noswear.csv',7), ('disability.csv',13), ('rsd.txt',14), ('ethnicity.csv', 15),('archaic.csv',16),('class.csv',17),('gender.csv',18),('religion.csv',19),('nationality.csv',20)]
    #Index Values [1, 4, 7, 13, 14, 15, 16, 17, 18, 19, 20]
    wordToFeature = defaultdict() #Word -> [Index X]
    counter = 1
    for f,idx in fileNames:
        words = open(directory+f, 'r').read()
        words = words.split(', ')
        for w in words:
            if w not in wordToFeature:
                wordToFeature[w] = set()
            wordToFeature[w].add(idx)
    return wordToFeature, max(fileNames, key=lambda x:x[1])[1]+1


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
13. Disability -hatebase + wiki
14. Racial Slurs DB
15. Ethics Slurs (WIKI) + hatebase
16. archaic -hatebase
17. class -hatebase
18. gender- hatebase and wiki
19. religion -hatebase
20. nationality
"""