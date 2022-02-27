def true_positive(y_true,y_pred):
    count = 0
    for yt, yp in zip(y_true,y_pred):
        if yt == yp == 1:
            count += 1 
    return count

def true_negative(y_true,y_pred):
    count = 0
    for yt, yp in zip(y_true,y_pred):
        if yt == yp == 0:
            count += 1 
    return count

def false_positive(y_true,y_pred):
    count = 0
    for yt, yp in zip(y_true,y_pred):
        if yt == 0:
            if yp == 1:
                count += 1 
    return count

def false_negative(y_true,y_pred):
    count = 0
    for yt, yp in zip(y_true,y_pred):
        if yt == 1:
            if yp == 0:
                count += 1 
    return count



l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]
print(true_positive(l1,l2))
print(false_positive(l1,l2))
print(false_negative(l1,l2))
print(true_negative(l1,l2))