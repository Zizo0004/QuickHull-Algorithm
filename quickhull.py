# Quick Hull algorithm for finding the convex hull of a set of points - ECM3428 – Algorithms that changed the world
# step 1. Find the min and max x values. forming a line segment that seperates the points into 2 subsets left and right
# step 2. for each subset, find the point that is farthest from the line segment
# step 3. repeat step 2 for the 2 new line segments
# step 4. repeat step 3 until no points are left
# step 5. terminate the algorithm 
import math

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)] # random points from an example i found online 
convex_hull = []
def findMaxDistance(min_x,max_x,points):
    # equation to find left / right side of line = (x2-x1).(y3-y1)-(y2-y1).(x3-x1)
    # Distance equation = |(x2-x1).(y3-y1)-(y2-y1).(x3-x1)| / sqrt((x2-x1)^2 + (y2-y1)^2)
    # The equation to use = |(min_x[0]-i[0]).(max_x[1]-i[1])-(min_x[1]-i[1]).(max_x[0]-i[0])| / sqrt((min_x[1]-i[0])^2 + (min_x[1]-i[1])^2)

    current_max_distance = 0
    set_of_points = None
    if len(points) > 0:
        for i in points:
            distance = abs((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) / math.sqrt((max_x[0] - min_x[0])**2 + (max_x[1] - min_x[1])**2)
            if distance > current_max_distance: 
                current_max_distance = distance
                set_of_points = i
        convex_hull.append(set_of_points)
    else:
        return None
    return set_of_points


def findConvexHull(points):
    # initial points, no importance
    min_x = points[0]
    max_x = points[-1]
    left_side = []
    right_side = []
    # finding the min and max x values
    for i in points:
        if i[0] < min_x[0]:
            min_x = i
        if i[0] > max_x[0]:
            max_x = i
    convex_hull.append(min_x)
    convex_hull.append(max_x)
    points.remove(min_x)
    points.remove(max_x)

    # equation to find left / right side of line = (x2-x1).(y3-y1)-(y2-y1).(x3-x1)
    # Distance equation = |(x2-x1).(y3-y1)-(y2-y1).(x3-x1)| / sqrt((x2-x1)^2 + (y2-y1)^2)
    for i in points:
        # positive score means it is the left side, else right side
        if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) > 0:
            left_side.append(i)
        else:
            right_side.append(i)
    findMaxDistance(min_x,max_x,left_side)
    findMaxDistance(min_x,max_x,right_side)

    print(convex_hull)
    print("hello")

