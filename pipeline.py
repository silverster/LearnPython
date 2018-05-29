import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:0.8812475333474292
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=BernoulliNB(alpha=10.0, fit_prior=True)),
    GradientBoostingClassifier(learning_rate=0.1, max_depth=9, max_features=1.0, min_samples_leaf=17, min_samples_split=15, n_estimators=100, subsample=0.5)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
