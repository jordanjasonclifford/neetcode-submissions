class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0

        # Start one pointer at the far right
        right = len(heights) - 1

        # This stores the maximum area we have found so far
        res = 0

        # Keep checking containers while the two pointers have not crossed
        while left < right:

            # The height of the container is limited by the shorter line.
            # The width is the distance between the two pointers.
            #
            # area = shorter height * width
            area = min(heights[left], heights[right]) * (right - left)

            # Update the best answer if this area is larger
            res = max(res, area)

            # Move the pointer with the smaller height.
            #
            # Why?
            # The width is going to shrink no matter what,
            # so we need to try to find a taller line to possibly get a bigger area.
            if heights[left] <= heights[right]:
                left += 1

            # If the right height is smaller, move the right pointer inward
            else:
                right -= 1

        # Return the largest area found
        return res