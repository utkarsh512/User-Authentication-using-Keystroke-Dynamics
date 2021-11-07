"""ANN for User Authentication

Author: Utkarsh Patel
This module is a part of MIES Term Project"""

import numpy as np
import argparse
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPClassifier
import pickle as pkl

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hidden_layers', nargs='+', type=int, required=True, help='dimension of hidden layers')
    parser.add_argument('--max_iter', type=int, default=500, help='maximum iterations to run')
    parser.add_argument('--random_state', type=int, default=42, help='seed for random number generation')
    args = parser.parse_args()

    # Reading the dataset
    x = pkl.load(open('data/x.pkl', 'rb'))
    y = pkl.load(open('data/y.pkl', 'rb'))
    np.random.RandomState(seed=args.random_state).shuffle(x)
    np.random.RandomState(seed=args.random_state).shuffle(y)

    # K-Fold cross validation
    kf = KFold(n_splits=5)
    train_acc, test_acc = 0, 0
    split_count = 0
    for train_index, test_index in kf.split(x):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf = MLPClassifier(hidden_layer_sizes=tuple(args.hidden_layers),
                            max_iter=args.max_iter,
                            random_state=args.random_state)
        clf.fit(x_train, y_train)
        cur_train_acc = clf.score(x_train, y_train)
        cur_test_acc = clf.score(x_test, y_test)
        split_count += 1
        print(f'Fold {split_count}:')
        print(f'\tTraining accuracy: {cur_train_acc}')
        print(f'\tTest accuracy: {cur_test_acc}\n')
        train_acc += cur_train_acc
        test_acc += cur_test_acc

    train_acc /= 5
    test_acc /= 5
    print('Five-fold cross validation result:')
    print(f'\tTraining accuracy: {train_acc}')
    print(f'\tTest accuracy: {test_acc}\n')
    print('DONE.')

if __name__ == '__main__':
    main()





