from sklearn.model_selection import StratifiedKFold
import pandas as pd

data = pd.read_csv(r'Cross Validation\Classification Data.csv')

# creating a new column in dataframe
data['Stratified kfold'] = -1

# random shuffle
data = data.sample(frac = 1).reset_index(drop = True)
X = data.drop(['5'] , axis = 1)
y= data['5']

# initiating StratifiedKFold
# while creating subset/fold, it will maintain the same ratio of class's values as in entire data

skfold = StratifiedKFold(n_splits=5)

# below, trn_ and val_ returns the index of rows which are part of training and validation
# fold will be fold number, ie., subset dataframe number.
for fold, (trn_ , val_) in enumerate(skfold.split(X= X, y = y)):
    data.loc[val_,'Stratified kfold'] = fold
    print(val_, fold)


data.to_csv(r'Cross Validation\Data with Stratified Kfold column.csv' , index = None)