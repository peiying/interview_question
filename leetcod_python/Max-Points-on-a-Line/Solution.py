# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        res = 0
        for i in xrange(len(points)):
            map = {'inf': 0}
            dup = 1
            for j in xrange(i + 1, len(points)):
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    map['inf'] += 1
                elif points[i].x != points[j].x:
                    key = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if key in map:
                        map[key] += 1
                    else:
                        map[key] = 1
                else:
                    dup += 1
            res = max(res, max(map.values()) + dup)
        return res
           
