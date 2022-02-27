from TP_TM_FP_FN import true_negative, true_positive, false_negative, false_positive


l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]


def accuracy(y_true, y_pred):
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    fn = false_negative(y_true, y_pred)

    return (tp+tn)/(tp+fp+tn+fn)

def precision(y_true, y_pred):
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    fn = false_negative(y_true, y_pred)

    return tp/(tp+fp)


def recall(y_true, y_pred):
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    fn = false_negative(y_true, y_pred)

    return tp/(tp+fn)

def f1_score(y_true, y_pred):
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)

    return (2*p*r)/(p+r)


l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]

print(accuracy(l1,l2))
print(precision(l1,l2))
print(recall(l1,l2))
print(f1_score(l1,l2))