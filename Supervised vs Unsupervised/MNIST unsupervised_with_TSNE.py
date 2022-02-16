# import required libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn import datasets
from sklearn import manifold


# fetching the data
data = datasets.fetch_openml(
    'mnist_784',
    version= 1,
    return_X_y= True )

# storing the data into variables
pixel_values, labels = data
pixel_values = pd.DataFrame(pixel_values)
labels = pd.DataFrame(labels.astype(int))   # this has the target variable

# below code to see pixels into image
single_image = np.array(pixel_values.iloc[0]).reshape(28,28)
plt.imshow(single_image)
# plt.show()

# below code is to change these many features into two using T-SNE
tsne = manifold.TSNE(n_components= 2, random_state= 123)
transformed_data = tsne.fit_transform(pixel_values[:3000])   # this means top 3000 rows and no slicing on columns

print(pd.DataFrame(transformed_data))
print(pd.DataFrame(labels[:3000]))

# lets again add two features from above and target variables in one dataframe
temp_data = np.column_stack((pd.DataFrame(transformed_data), labels[:3000]))
final_data = pd.DataFrame(temp_data , columns = ['X', 'y', 'labels'])
print(final_data.head(10))

grid = sns.FacetGrid(final_data, hue = 'labels' , size = 8)
grid.map(plt.scatter, 'X' , 'y').add_legend()
grid.show()