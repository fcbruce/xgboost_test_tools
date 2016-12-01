#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Thu 01 Dec 2016 15:04:46
#
#

import json
import numpy as np

import map_rule as mr

feature_file = '../feature/loan_credit_feature1201.txt'
output_file = '../data/1201.npy'
rule_file = '../rule/rule'

fin = open(feature_file, 'r')
rin = open(rule_file, 'r')

rules = [line[:-1].split(',') for line in rin]

features = [json.loads(line) for line in fin]

rows = []


for f in features:
    row = []
    for rule in rules:
        result = float(rule[1])
        if (f.get(rule[0]) != None):
            if rule[2] == 'one_to_one_map':
                result = mr.one_to_one_map(f[rule[0]])
            elif rule[2] == 'gender_map':
                result = mr.gender_map(f[rule[0]])
            elif rule[2] == 'one_hot':
                result = mr.one_hot(f[rule[0]], int(rule[3]))

        row.append(result)

    rows.append(row)


rows = np.array(rows)

np.save(output_file, rows)
            

