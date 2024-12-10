# Quick Hull algorithm for finding the convex hull of a set of points - ECM3428 – Algorithms that changed the world
# step 1. Find the min and max x values. forming a line segment that seperates the points into 2 subsets left and right
# step 2. for each subset, find the point that is farthest from the line segment
# step 3. repeat step 2 for the 2 new line segments
# step 4. repeat step 3 until no points are left
# step 5. terminate the algorithm 

import math
convex_hull = []
# finding the max distance between the line segments of min and max x and the remaining points.
def findMaxDistance(min_x, max_x, side):
    current_max_distance = 0
    point = None
    
    for i in side:
        # Calculate the cross product to find the perpendicular distance
        cross_product = abs((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - 
                          (max_x[1] - min_x[1]) * (i[0] - min_x[0]))
        
        # Calculate the base length
        base_length = math.sqrt((max_x[0] - min_x[0])**2 + (max_x[1] - min_x[1])**2)
        
        # Calculate perpendicular distance
        if base_length != 0:  # Avoid division by zero
            distance = cross_product / base_length
            print(distance)
            if distance > current_max_distance:
                current_max_distance = distance
                point = i
    
    # Only include points that are actually outside the current hull
    if point is not None and current_max_distance > 0.0001:  # Use small epsilon to handle floating point comparison
        if point not in convex_hull:
            try:
                side.remove(point)
                convex_hull.append(point)
            except ValueError:
                pass  # Point might have been removed already
            
    return point, side

def split_set(min_x,max_x,set):
    subset = []
    for i in set:
        if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) > 0:
            subset.append(i)
    return subset 

def findConvexHull(points,min_x,max_x):
    current_node = 0
    # Base case, when points are 1, add to convex hull and stop recursion
    if len(points) == 1:
        if points[0] not in convex_hull:
            convex_hull.append(points[0])
        return convex_hull
    # Base case, when points are empty stop recursion
    if len(points) == 0:
        return convex_hull
    else:    
        current_node,subset = findMaxDistance(min_x,max_x,points)
        if current_node is not None:
            first_subset = split_set(min_x,current_node,points)
            findConvexHull(first_subset,min_x,current_node)

            second_subset = split_set(current_node,max_x,points)
            findConvexHull(second_subset,current_node,max_x)
    return convex_hull

def main(points):
    # Initalization step of the code. Min x and max x points are found, and the set of points are split into left and right subsets.
    left_side = []
    right_side = []
    min_x = points[0] # random value s 
    max_x = points[-1]

    if not points:
        return convex_hull

    # find the min x and max x based on the inital set of points
    for i in points:
        if i[0] < min_x[0]:
            min_x = i
        if i[0] > max_x[0]:
            max_x = i
    convex_hull.append(min_x)
    convex_hull.append(max_x)

    remaining_points = points.copy()
    remaining_points.remove(min_x)
    remaining_points.remove(max_x)

    for i in points:
        if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) > 0:
            left_side.append(i)
        elif ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) < 0:
            right_side.append(i)

    # recursively find convex hull points for left and right subset
    findConvexHull(left_side, min_x, max_x)
    findConvexHull(right_side, max_x, min_x)

    return convex_hull

points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 4), (4, 0)]
print(main(points))
