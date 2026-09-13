class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1,2]
        ways = 0
        if n == 1:
            return 1
        else:
            for stair in range(n):
                if stair == 0:
                    continue
                elif stair == 1:
                    continue
                else: 
                    ways = arr[stair-1] + arr[stair-2] 
                    arr.append(ways)
            print(arr)
            return arr.pop()      
