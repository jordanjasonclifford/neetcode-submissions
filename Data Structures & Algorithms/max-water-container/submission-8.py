class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start one pointer at the leftmost vertical line.
        left = 0

        # Start the other pointer at the rightmost vertical line.
        right = len(heights) - 1

        # Store the largest container area found so far.
        res = 0

        # Continue until the two pointers meet.
        while left < right:

            # The container's height is limited by the shorter of the two lines.
            container_height = min(heights[left], heights[right])

            # The container's width is the distance between the two pointers.
            container_width = right - left

            # Calculate the area formed by the current pair of lines.
            area = container_height * container_width

            # Update the maximum area if the current area is larger.
            res = max(res, area)

            # Move the pointer pointing to the shorter line.
            #
            # Moving the taller line would only reduce the width while the
            # shorter line would still limit the container's height.
            #
            # By moving the shorter line, we may find a taller line that
            # compensates for the reduced width and creates a larger area.
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # Return the largest container area found.
        return res