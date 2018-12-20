# ToxicDetector

4 Importand Files: 

1.utils.py

2.baseline.ipynb

3.OtherClassifiers.ipynb 

4.Word Embedding.ipynb

## utils.py
Contains the code that is used to parse the input pandas dataframe into the feature vectors based on the feature engineering input method. 

## baseline.ipynb
- Reads train/test .csv file into pandas dataframe
- Uses utils.py to get feature vector transformation
- Defines the baseline NN model and the trainer for it 
- Preforms training and test on the starter baseline parameters
- Hyper parameter search to find the best models based on 5 fold cross validation 
- Takes best hyperparam and train on full dataset and then output to file the prediction
- Tries hyper parameter search again but with ROC AUC validation score
- Output best model's test prediction to file 

## OtherClassifiers.ipynb 

## Word Embedding.ipynb
- Reads in csv into dataframe
- Does preprocessing to build a vocab set
- Pull word embeddings from GloVE file that match, others are randomized to make embedding weights
- Defines the WeNN model and Trainer, with embedding layer pre-initialized 
- Runs the starter parameters and Tests
- Hyperparameter search again, but smaller scale 
- Runs best model on test

