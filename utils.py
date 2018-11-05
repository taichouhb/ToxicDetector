import numpy as np
import pandas as pd


def featurize(input):
    #Takes in Nx (2) array of tuples. 
    
    # Parse input sentence into D features for each sentence  
    x, y = feats(input)
    
    
    #Perhaps need to take mini-batches, or we can train on the whole thing
    #Split by sampling into three sets train, val, test
    
    
    #Return data_train, data_val, data_test subsets of full data, 
    #data_train being largest, probably  
    return x, y

def populateGlobalTable():
    #TODO: Populate the hash table that contains the mappings of words to features
    #Update the feature to index comment at the bottom when you finish one website source
    #Returns the feature table, as well as the total number of features we've supported so far
    return {}, 0

def countFeats(input):
    #Parse input into features of length D.
    #Pandas DF N x 3 
    globalTable, totalFeatures = populateGlobalTable()
    featureMatrix = []
    labels = []
    for ind, row in input.iterrows():
        featureVector = np.array([0]*totalFeatures)
        idd, comment = row['id'], row['comment_text']
        label = [row['toxic'], row['severe_toxic'], row['obscene'], \
                 row['threat'], row['insult'], row['identity_hate']]
        #Tokenize comment
        newSet = ',.!?\"'
        exclamation = comment.count("!")
        table =  str.maketrans({key:None for key in newSet})
        translated = comment.translate(table)
        tokens = translated.split(" ")
        for t in tokens: 
            if t in globalTable:
                for ind in globalTable[t]:
                    featureVector[ind] += 1 
        featureMatrix.append(featureVector)
        labels.append(label)
        
    featureMatrix = np.array(featureMatrix)
    labels = np.array(labels)
    return featureMatrix, labels
      
    
    
    #output returns in N x D, N (labels, N of them)
    #Perhaps preprocess the labels here so they are binary class, instead of 10 classes
    return None, None

def feats(input):
    x, y = countFeats(input)
    #Are we doing other types of features that aren't counts?
    #Add them here... 
    
    return x,y
    

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

Index of actual features implemented: 
(Index - Name of Source (description) )
1-
2-
3-
...

"""