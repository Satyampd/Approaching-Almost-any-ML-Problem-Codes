from sklearn.model_selection import KFold
import pandas as pd

data = pd.read_csv(r'Cross Validation\Classification Data.csv')

# creating a new column in dataframe
data['kfold'] = -1

# random shuffle
data = data.sample(frac = 1).reset_index(drop = True)

# initiating KFold
kfold = KFold(n_splits=5)


# below, trn_ and val_ returns the index of rows which are part of training and validation
# fold will be fold number, ie., subset dataframe number.
for fold, (trn_ , val_) in enumerate(kfold.split(X= data)):
    data.loc[val_,'kfold'] = fold
    print(val_, fold)

data.to_csv(r'Cross Validation\Data with Kfold column.csv' , index = None)