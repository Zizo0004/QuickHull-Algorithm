import unittest
import quickhull

class TestQuickhull(unittest.TestCase):
    def test1_quickhull(self):
        points = [(0,0), (1,1), (2,2), (1,2), (2,0)]
        expected = {(0,0), (2,0), (2,2), (1,2)}
        result = set(quickhull.findConvexHull(points,(0,0),(2,0)))
        self.assertEqual(result, expected)
    def test_case_2(self):
        points = [(1,1), (3,1), (2,2), (2,0)]
        expected = {(1,1), (3,1), (2,2), (2,0)}
        result = set(quickhull.findConvexHull(points,(1,1),(3,1)))
        self.assertEqual(result, expected)

    def test_case_3(self):
        points = [(0,0), (3,0), (3,3), (0,3), (1,1), (2,2)]
        expected = {(0,0), (3,0), (3,3), (0,3)}
        result = set(quickhull.findConvexHull(points,(0,0),(3,0)))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()        