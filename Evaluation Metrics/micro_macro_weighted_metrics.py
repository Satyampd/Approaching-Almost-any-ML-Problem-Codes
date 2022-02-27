from tkinter import Y
import numpy as np
from accuracy_precision_recall_f1 import precision,recall,f1_score
from TP_TM_FP_FN import true_negative, true_positive, false_negative, false_positive
from collections import Counter


y_true = [0,1,2,0,1,2,0,2,2]
y_pred = [0,2,1,0,2,1,0,0,2]

# Macro Precision
# ---> Calculate Precision Individually and then average them with no of classes

def macro_precision(y_true,y_pred):
    temp_precision = 0
    classes = np.unique(y_true)
    for class_ in classes:
        y_true_for_class = [1 if val==class_ else 0 for val in y_true]
        y_pred_for_class = [1 if val==class_ else 0 for val in y_pred]
        temp_precision +=   precision(y_true_for_class,y_pred_for_class)
    return temp_precision/len(np.unique(y_true))

def micro_precision(y_true,y_pred):
    temp_tp = 0
    temp_fp = 0
    classes = np.unique(y_true)
    for class_ in classes:
        y_true_for_class = [1 if val==class_ else 0 for val in y_true]
        y_pred_for_class = [1 if val==class_ else 0 for val in y_pred]
        temp_tp +=   true_positive(y_true_for_class,y_pred_for_class)
        temp_fp +=   false_positive(y_true_for_class,y_pred_for_class)
    return temp_tp/(temp_tp+temp_fp)

def weighted_precision(y_true,y_pred):
    temp_precision = 0
    weighted_precision = 0
    classes = np.unique(y_true)
    class_counts = Counter(y_true)
    for class_ in classes:
        y_true_for_class = [1 if val==class_ else 0 for val in y_true]
        y_pred_for_class = [1 if val==class_ else 0 for val in y_pred]
        temp_precision =   precision(y_true_for_class,y_pred_for_class)
        weighted_precision += temp_precision * class_counts[class_]

    return weighted_precision/len(y_true)


print(macro_precision(y_true, y_pred))
print(micro_precision(y_true, y_pred))
print(weighted_precision(y_true, y_pred))

