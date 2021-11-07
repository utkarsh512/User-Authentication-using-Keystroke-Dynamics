"""Module for preparing dataset for ANN

Author: Utkarsh Patel
This module is port of MIES Term Project"""

import pandas as pd
import numpy as np
import pickle as pkl
from tqdm import tqdm

LABELS = {'18EC10006': 0,
          '18EC10020': 1,
          '18EC10028': 2,
          '18EC10063': 3,
          '18EC10067': 4,
          '18EC10073': 5,
          '18EC10078': 6,
          '18EC35034': 7
          }

FEATURE_COUNT = [30, 32, 28, 26, 26, 10, 8, 20]    # Count of features for each user

def main():
    x, y = [], []                                  # feature vectors and target labels
    data_dir = 'data/{0}/after_{1}_{2}.csv'
    total_feature_count = 0
    for cnt in FEATURE_COUNT:
        total_feature_count += cnt
    with tqdm(total=total_feature_count) as pbar:
        for user in LABELS.keys():
            for k in range(FEATURE_COUNT[LABELS[user]]):
                x_ = []
                df = pd.read_csv(data_dir.format(user, 'hold', k + 1))
                x_.extend(df.to_numpy().flatten().tolist())
                df = pd.read_csv(data_dir.format(user, 'distances', k + 1))
                x_.extend(df.to_numpy().flatten().tolist())
                x.append(np.array(x_))
                y.append(LABELS[user])
                pbar.update(1)
    x = np.array(x)
    y = np.array(y)
    pkl.dump(x, open('data/x.pkl', 'wb'))
    pkl.dump(y, open('data/y.pkl', 'wb'))

if __name__ == '__main__':
    main()