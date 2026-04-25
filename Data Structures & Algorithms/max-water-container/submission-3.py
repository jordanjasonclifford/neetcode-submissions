class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # start pointers at both ends of the array
        left = 0
        right = len(heights) - 1

        # store max area found
        res = 0

        # keep moving pointers until they meet
        while left < right:

            # width = distance between pointers
            # height = min of the two walls (water limited by shorter wall)
            area = (right - left) * min(heights[left], heights[right])

            # update max area
            res = max(res, area)

            # move the pointer with the smaller height
            # because that's the limiting factor
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res


        