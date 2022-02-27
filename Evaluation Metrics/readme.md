## Evaluation Metrics Notes

## How to find optimal threshold for PR Curve:
Here are 2 ways to find the optimal threshold:

[More info on PR Curve](https://analyticsindiamag.com/complete-guide-to-understanding-precision-and-recall-curves/)    
![alt text](https://lh5.googleusercontent.com/i01nrezxO9CJc4Jh3v9r1soCzCwAkk4R_g4WCH81CgsF0332e1wuapNU7d7CkhpC_8V2DxXIJPI5fHSUeTE7ziDwGeX56wcZWvzyflcBKOYCPAaONuhUvNjmhTW0Yp_devijiNfJ)


1. Find the euclidean distance of every point on the curve, which is denoted by (recall, precision) for a corresponding threshold, from (1,1). Pick the point and the corresponding threshold, for which the distance is minimum.
2. Find F1 score for each point (recall, precision) and the point with the maximum F1 score is the desired optimal point.