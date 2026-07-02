class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0
        right = len(numbers) - 1
        newLst = []

        # it's sorted, so go through by two pointer approach
        while left < right:

            # the two sum
            sum = numbers[left] + numbers[right]


            if sum == target:
                # as question requires the indices to be increased
                left += 1
                right += 1

                newLst.append(left)
                newLst.append(right)
                return newLst

            # left needs to be increased to get bigger
            elif sum < target:
                left += 1

            # same way, opposite, needs to get smaller
            else:
                right -= 1

        return newLst