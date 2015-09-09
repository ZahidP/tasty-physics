# Description: Examines, plots, and analyzes features
# in physics dataset.

def main(classifierType,variables):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import sys

    from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    train = pd.read_csv('../data/training.csv', index_col='id')

    # defualt to gradient boosting if nothing is provided
    # classifierType = sys.argv[1] if (len(sys.argv) > 1) else 'gb'

    # do not include last 5 columns because
    # variables = train.columns[0:-5]

    if classifierType == 'gb':
        baseline = GradientBoostingClassifier(n_estimators=50, learning_rate=0.005, subsample=0.7,
                                          min_samples_leaf=10, max_depth=7, random_state=11)
    elif classifierType == 'rf':
        baseline = RandomForestClassifier(n_estimators=25)


    baseline.fit(train[variables], train['signal'])
    # sort importances
    indices = np.argsort(baseline.feature_importances_)
    # plot as bar chart
    plt.barh(np.arange(len(variables)), baseline.feature_importances_[indices])
    plt.yticks(np.arange(len(variables)) + 0.25, np.array(variables)[indices])
    _ = plt.xlabel('Relative importance: ' + classifierType)
    plt.savefig("feature_Importance_" + classifierType + ".png")

    return baseline
