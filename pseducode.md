# Quick Hull Algorithm --- Pseudocode implementation
```pseudo

function findMaxDistance(min_x, max_x, side)
    current_max_distance ← 0
    point ← 0
    for each i in side do
        distance ← |(max_x.x - min_x.x) * (i.y - min_x.y) - 
                    (max_x.y - min_x.y) * (i.x - min_x.x)| /
                   sqrt((max_x.x - min_x.x)^2 + (max_x.y - min_x.y)^2)
        
        if distance ≥ current_max_distance then
            current_max_distance ← distance
            point ← i
        end if
    end for
    remove point from side
    add point to convex_hull
    return point, side
end function


function split_set(min_x, max_x, set)
    subset ← empty list
    for each i in set do
        if ((max_x.x - min_x.x) * (i.y - min_x.y) - 
            (max_x.y - min_x.y) * (i.x - min_x.x)) > 0 then
            add i to subset
        end if
    end for
    return subset
end function


function findConvexHull(points, min_x, max_x)
    if length(points) = 1 then
        add points[0] to convex_hull
        return convex_hull
    end if

    # termination step
    if length(points) = 0 then
        return convex_hull
    end if
    else
        current_node, subset ← findMaxDistance(min_x, max_x, points)

        # split the subset into two new subsets based on the new line segment
        first_subset ← split_set(min_x, current_node, points)
        call findConvexHull(first_subset, min_x, current_node)

        second_subset ← split_set(current_node, max_x, points)
        call findConvexHull(second_subset, current_node, max_x)
    end else
end function


# initialize steps before recursion

points ← [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

left_side ← empty list
right_side ← empty list
convex_hull ← empty list

min_x ← points[0]
max_x ← points[-1]

# find the min x and max x based on the inital set of points

for each i in points do
    if i[0] < min_x[0] then
        min_x ← i
    end if
    if i[0] > max_x[0] then
        max_x ← i
    end if
end for

add min_x to convex_hull
add max_x to convex_hull
remove min_x from points
remove max_x from points

# partition the remaining points into left_side and right_side
for each i in points do
    if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - 
        (max_x[1] - min_x[1]) * (i[0] - min_x[00])) > 0 then
        add i to left_side
    else if ((max_x[0] - min_x[0]) * (i[1] - min_x[1]) - 
             (max_x[1] - min_x[1]) * (i.x - min_x[0])) < 0 then
        add i to right_side
    end if
end for

# recursively find convex hull points for left and right subset
call findConvexHull(left_side, min_x, max_x)
call findConvexHull(right_side, max_x, min_x)

