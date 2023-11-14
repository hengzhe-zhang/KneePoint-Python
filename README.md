## KneePoint-Python
This Python package is designed for detecting knee points in PF.

### Knee Point Detection Methods:
1. **Angle-Based Detection**
   - Bend Angle Knee: This method utilizes the angle between a point and its neighboring points or extreme points to identify knee points.

2. **Euclidean Distance-Based Detection**
   - Euclidean distance: This method leverages Euclidean distance for knee point identification.
   - Manhattan distance: This method relies on Manhattan distance for knee point identification.

### No Knee Point Model Selection Method:
  - Harmonic Rank: This method, used in the GECCO 2022 Symbolic Regression Competition, employs the best harmonic mean rank of models for model selection.

### Usage Instructions:
The package automatically normalizes points before selecting knee points.

```python
from bend_angle_knee import find_knee_based_on_bend_angle

# Pareto points
pareto_points = [[1, 5], [2, 4], [3, 2], [4, 1]]

# Detecting the knee point
knee, index = find_knee_based_on_bend_angle(pareto_points)
print(f"Knee point: {knee}, Index: {index}")
```
