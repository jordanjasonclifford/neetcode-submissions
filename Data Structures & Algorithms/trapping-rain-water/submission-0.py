class Solution:
    def trap(self, height: List[int]) -> int:
        
        # edge case: no bars, no water
        if not height:
            return 0

        # two pointers starting from both ends
        left = 0
        right = len(height) - 1

        # track the highest wall seen so far from each side
        leftMax = height[left]
        rightMax = height[right]

        # total trapped water
        res = 0

        # move pointers inward
        while left < right:

            # always process the smaller side
            # because water is limited by the shorter boundary
            if leftMax < rightMax:

                left += 1

                # update max height seen from left
                leftMax = max(leftMax, height[left])

                # water trapped at this index = leftMax - current height
                res += leftMax - height[left]

            else:
                right -= 1

                # update max height seen from right
                rightMax = max(rightMax, height[right])

                # water trapped at this index = rightMax - current height
                res += rightMax - height[right]

        return res