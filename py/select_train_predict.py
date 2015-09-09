import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
###
import evaluation
import check_tests as ct
import features
###
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import roc_curve, auc


train = pd.read_csv('../data/training.csv', index_col='id')
subset = [1,2,3,4,5]
variables = train.columns[subset]

trained_model = features.main('rf', variables)
ct.agreement(trained_model, variables)
ct.correlation(trained_model, variables)
ct.weightedAuc(trained_model, variables, train)
