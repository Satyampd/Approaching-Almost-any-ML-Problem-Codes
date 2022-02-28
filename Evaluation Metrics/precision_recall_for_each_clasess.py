
## TODO: Precision and Recall for Individual classes same as classification_report
import numpy as np
from sklearn.metrics import classification_report


def true_positive(y_true,y_pred, class_):
    count = 0
    for yt, yp in zip(y_true,y_pred):
        if yt == yp == class_:
            count += 1 
    return count

def false_positive(y_true,y_pred, class_):
    count = 0
    for yt, yp in zip(y_true,y_pred):
        if yt != class_:
            if yp == class_:
                count += 1 
    return count


def precision(y_true, y_pred, class_):
    tp = true_positive(y_true, y_pred, class_)
    fp = false_positive(y_true, y_pred, class_)
    return tp/(tp+fp)


l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]

for class_ in np.unique(l1):
    print(f"Class {class_} has Precision of: {round(precision(l1,l2,class_),2)}")


print(classification_report(l1,l2))