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
    
    
    
    #output returns in N x D, N (labels, N of them)
    #Perhaps preprocess the labels here so they are binary class, instead of 10 classes
    return None, None