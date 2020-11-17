"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

 

Note:

    All the input integers are in the range [-10000, 10000].
    A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    Input points have no order.
"""



class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        import math 
        import itertools 

        pts = [p1, p2, p3, p4]


        for i in range(4): 

            dists = list() 
            for j in range(4): 

                if i == j: 
                    continue 

                pt1 = pts[i]
                pt2 = pts[j]

                # distance from i to j
                d = math.sqrt( ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2) )
                dists.append(d)


            # Sides not equal length 
            if len(set(dists)) != 2: 
                return False  



        tmp = itertools.permutations(pts, 3)
        angles = list() 
        for item in tmp:
            angles.append(get_angle(item[0], item[1], item[2]))


        if sum([math.isclose(ang, 90) for ang in angles]) != 4: 
            return False

        return True 



def get_angle(a, b, c): 
    import math 

    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang






if __name__ == "__main__": 

    p1, p2, p3, p4 = [-2009,2747], [-1566,2436], [-2320,2304], [-1877,1993]
    soln = Solution()

    a = soln.validSquare(p1, p2, p3, p4)
    print(a)
