# test.py

import unittest
from quickhull import findMaxDistance, split_set, findConvexHull, main

class TestQuickHull(unittest.TestCase):

    def setUp(self):
        # must reset the hull before each test due to previous errors in appending and removing
        from quickhull import convex_hull
        convex_hull.clear()

    def test_findMaxDistance(self):
        side = [(1, 3), (2, 4), (3, 1)]
        point, remaining_side = findMaxDistance((0, 0), (4, 2), side.copy())

        self.assertEqual(point, (2, 4))
        self.assertEqual(sorted(remaining_side), sorted([(1, 3), (3, 1)]))

    def test_split_set(self):
        set_points = [(1, 1), (2, 2), (3, 3)]
        subset = split_set((0, 0), (4, 4), set_points)
        self.assertEqual(subset, [])

    # testing findconvexhull with collinear points, points laying on the line segement
    def test_findConvexHull_with_colinear_points(self):
        points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        hull = main(points.copy())
        expected_hull = [(0, 0), (4, 4)]
        self.assertEqual(sorted(hull), sorted(expected_hull))

    # Testing findconvexhull with a lot of points
    def test_findConvexHull_with_more_points(self):
        points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 4), (4, 0)]
        hull = main(points.copy())
        expected_hull = [(0, 0), (4, 4), (0, 4), (4, 0)]
        self.assertEqual(sorted(hull), sorted(expected_hull))

if __name__ == '__main__':
    unittest.main()
