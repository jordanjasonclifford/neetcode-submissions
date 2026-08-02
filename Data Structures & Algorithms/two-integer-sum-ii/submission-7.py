class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0
        right = len(numbers) - 1
        

        while left < right:

            sum = numbers[left] + numbers[right]

            if sum == target:

                # numbers need to be added 
                left += 1
                right += 1
                return [left, right]

            elif sum < target:

                left += 1

            else:

                right -= 1

        return []