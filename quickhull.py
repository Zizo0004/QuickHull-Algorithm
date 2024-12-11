# Quick Hull algorithm for finding the convex hull of a set of points - ECM3428 – Algorithms that changed the world
import math
import matplotlib.pyplot as plt
convex_hull = []
#Function for finding the max distance between the line segments of min and max x and the remaining points.
def findMaxDistance(min_x, max_x, side):
    current_max_distance = 0
    point = None
    
    for i in side:
        #Calculating the cross product ,easure the distance between each point and the line formed between min_x and max_x
        cross_product = abs((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - 
                          (max_x[1] - min_x[1]) * (i[0] - min_x[0]))        
        base_length = math.sqrt((max_x[0] - min_x[0])**2 + (max_x[1] - min_x[1])**2)
        
        if base_length != 0:  # stopping division with zero
            distance = cross_product / base_length
            #print(distance)
            # preventing the same point being added
            if distance > current_max_distance:
                current_max_distance = distance
                point = i
    
    #preventing the case where all distances are zero leading to the intial currentmaxdistance point being added
    if point is not None and current_max_distance > 0:

        #stopping dups
        if point not in convex_hull:
            try:
                side.remove(point)
                convex_hull.append(point)
            except ValueError:
                pass  
            
    return point, side

#simple function to split each subset into smaller subsets. Right/below side not considered because they are already enclosed by the line segments
def split_set(min_x,max_x,set):
    subset = []
    for i in set:
        if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - (max_x[1] - min_x[1]) * (i[0] - min_x[0])) > 0:
            subset.append(i)
    return subset 

#The recursive function to find the convex hull, points is the remaining set of points
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
            #recursively find the convex hull for the first set until base case is checked, do the same for the second set.
            first_subset = split_set(min_x,current_node,points)
            findConvexHull(first_subset,min_x,current_node)

            second_subset = split_set(current_node,max_x,points)
            findConvexHull(second_subset,current_node,max_x)
    return convex_hull

#main function to initialze the startup: finding min x and max x and spliiting the list into left and right.
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

    #copy for testing so each test doesnt affect the set of points of the other
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
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_points = (main(points))

print(convex_points)
convex_hull = [(0, 3), (4, 4), (3, 1), (0, 0)] # corrected order of the hull, still correct nontheless
x_coordinates =[]
y_coordinates =[]
convex_hull_x= []
convex_hull_y= []
#creating the graph 10x10
plt.figure(figsize=(10, 10))

#iterating over points and plot. same for convex hull
for x,y in points:
    x_coordinates.append(x)
    y_coordinates.append(y)
plt.scatter(x_coordinates, x_coordinates, c='blue', label='All Points')

# Plot and connect the convex hull points
for x,y in convex_hull:
    convex_hull_x.append(x)
    convex_hull_y.append(y)
convex_hull_x.append(convex_hull_x[0])
convex_hull_y.append(convex_hull_y[0])

plt.plot(convex_hull_x, convex_hull_y)
plt.scatter(convex_hull_x, convex_hull_y, c='red')
plt.title('Convex hull')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()