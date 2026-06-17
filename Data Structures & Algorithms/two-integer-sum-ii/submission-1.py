class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0
        right = len(numbers) - 1
        newLst = []


        while left < right:

            sum = numbers[left] + numbers[right]

            if sum == target:
                left += 1
                right += 1

                newLst.append(left)
                newLst.append(right)
                return newLst

            elif sum < target:
                left += 1

            else:
                right -= 1

        return newLst