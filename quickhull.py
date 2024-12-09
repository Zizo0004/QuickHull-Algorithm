# Quick Hull algorithm for finding the convex hull of a set of points - ECM3428 – Algorithms that changed the world
# step 1. Find the min and max x values. forming a line segment that seperates the points into 2 subsets left and right
# step 2. for each subset, find the point that is farthest from the line segment
# step 3. repeat step 2 for the 2 new line segments
# step 4. repeat step 3 until no points are left
# step 5. terminate the algorithm 

import math
def findMaxDistance(min_x,max_x,side):
    # Distance equation = |(x2-x1).(y3-y1)-(y2-y1).(x3-x1)| / sqrt((x2-x1)^2 + (y2-y1)^2)
    current_max_distance = 0
    point = 0
    for i in side:
            distance = abs((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) / math.sqrt((max_x[0] - min_x[0])**2 + (max_x[1] - min_x[1])**2)
            if distance >= current_max_distance: 
                current_max_distance = distance
                point = i
    side.remove(point)
    convex_hull.append(point) 
        
    return point, side

def split_set(min_x,max_x,set):
    subset = []
    for i in set:
        if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) > 0:
            subset.append(i)
    return subset 

def findConvexHull(points,min_x,max_x):
    current_node = 0
    if len(points) == 1:
        convex_hull.append(points[0])
        return convex_hull

    # if the subsets are empty, return the convex hull - Base case
    print("Points: ",len(points))
    if len(points) == 0:
        return convex_hull
    else:    
        current_node,subset = findMaxDistance(min_x,max_x,points)
        first_subset = split_set(min_x,current_node,points)
        findConvexHull(first_subset,min_x,current_node)

        second_subset = split_set(current_node,max_x,points)
        findConvexHull(second_subset,current_node,max_x)


points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

left_side = []
right_side = []
convex_hull = []
min_x = points[0]
max_x = points[-1]

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

for i in points:
    if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) > 0:
        left_side.append(i)
    elif ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) < 0:
        right_side.append(i)
findConvexHull(left_side,min_x,max_x)
findConvexHull(right_side,max_x,min_x)
print("Convex Hull: ",convex_hull) 
# expected [(0, 0), (0, 3), (3, 1), (4, 4)]
# output   [(0, 3), (4, 4), (0, 0), (3, 3), (3, 1), (2, 2)]

# points = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)]