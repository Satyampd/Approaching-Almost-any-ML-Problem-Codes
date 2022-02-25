## Evaluation Metrics Notes

## How to find optimal threshold for PR Curve:
Here are 2 ways to find the optimal threshold:

1. Find the euclidean distance of every point on the curve, which is denoted by (recall, precision) for a corresponding threshold, from (1,1). Pick the point and the corresponding threshold, for which the distance is minimum.
2. Find F1 score for each point (recall, precision) and the point with the maximum F1 score is the desired optimal point.