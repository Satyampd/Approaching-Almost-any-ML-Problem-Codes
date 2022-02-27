from sklearn.metrics import precision_recall_curve


y_true = [1,1,0,1,0,0,0,0,1,1]
y_pred_prob = [0.5,0.69,0.80,0.9,0.3,0.4,0.6,0.3,0.3,0.60]

precision, recall, thresholds = precision_recall_curve(y_true, y_pred_prob)
print(precision, recall, thresholds)