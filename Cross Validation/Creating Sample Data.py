
# create a binary classification dataset
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
# generate 2 class dataset
X, y = make_classification(n_samples=100, n_classes=4, weights=[0.40, 0.10, 0.30, 0.20 ],
    n_clusters_per_class=1, n_features=5)

data = np.column_stack((X,y))
pd.DataFrame(data).to_csv(r'Cross Validation\Data.csv' , index = None)

