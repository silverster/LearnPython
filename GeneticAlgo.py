from tpot import TPOTClassifier
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

#Load data
telescope = pd.read_csv('magic04data.csv')

#clean the data
telescope_shuffle = telescope.iloc[np.random.permutation(len(telescope))]
tele = telescope_shuffle.reset_index(drop=True)

#store 2 classes
tele['class'] = tele['class'].map({'g':0,'h':1})
tele_class = tele['class'].values

#split data
training_indices,validation_indices=training_indices,testing_indices = train_test_split(tele.index,stratify=tele_class,train_size=0.75)

#find best model
tpot = TPOTClassifier(generations=5,verbosity=2)
tpot.fit(tele.drop('class',axis=1).loc[training_indices].values,
	tele.loc[training_indices,'class'].values)

#accuracy scoring
tpot.score(tele.drop('class',axis=1).loc[validation_indices].values,
	tele.loc[validation_indices,'class'].values)

#Expot
tpot.export('pipeline.py')