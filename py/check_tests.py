import pandas as pd
import numpy as np
import evaluation
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import roc_curve, auc

def agreement(baseline,variables):
    check_agreement = pd.read_csv('../data/check_agreement.csv', index_col='id')
    agreement_probs = baseline.predict_proba(check_agreement[variables])[:, 1]

    ks = evaluation.compute_ks(
        agreement_probs[check_agreement['signal'].values == 0],
        agreement_probs[check_agreement['signal'].values == 1],
        check_agreement[check_agreement['signal'] == 0]['weight'].values,
        check_agreement[check_agreement['signal'] == 1]['weight'].values)
    print('KS metric', ks, ks < 0.09)


def correlation(baseline,variables):
    check_correlation = pd.read_csv('../data/check_correlation.csv', index_col='id')
    correlation_probs = baseline.predict_proba(check_correlation[variables])[:, 1]
    cvm = evaluation.compute_cvm(correlation_probs, check_correlation['mass'])
    print('CvM metric', cvm, cvm < 0.002)


def weightedAuc(baseline,variables,train):
    train_eval = train[train['min_ANNmuon'] > 0.4]
    train_probs = baseline.predict_proba(train_eval[variables])[:, 1]
    AUC = evaluation.roc_auc_truncated(train_eval['signal'], train_probs)
    print('AUC', AUC)
