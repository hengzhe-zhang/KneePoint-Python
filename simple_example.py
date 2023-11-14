from bend_angle_knee import find_knee_based_on_bend_angle

pareto_points = [[1, 5], [2, 3.5], [2.5, 2], [5, 1]]
knee, index = find_knee_based_on_bend_angle(pareto_points)
print(f"Knee point: {knee}, Index: {index}")