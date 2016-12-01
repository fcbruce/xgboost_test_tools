#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Thu 01 Dec 2016 17:01:56
#
#

import xgboost as xgb
import numpy as np
import math

rows_file = '../data/1201.npy'
model_file = '../models/RiskModel20161124.model'

def sigmoid(x):
    return 1. / (1 + np.exp(-x))

rows = np.load(rows_file)

mat = xgb.DMatrix(rows)

bst = xgb.Booster(model_file=model_file)
print sigmoid(bst.predict(mat))
