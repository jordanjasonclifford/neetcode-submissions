class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers. One in the beginning of the array, and one
        # at the end.
        lower, upper = 0, len(numbers) - 1
        while True:
            if numbers[lower] + numbers[upper] > target:
                upper -= 1
            elif numbers[lower] + numbers[upper] < target:
                lower += 1
            else:
                return [lower + 1, upper + 1]
