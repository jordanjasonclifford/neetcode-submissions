class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0

        right = len(numbers) - 1

        newLst = []


        while left < right:

            sum = numbers[left] + numbers[right]

            if sum == target:
                
                # question calls for the indice to be +1
                left += 1
                right += 1

                # add them to the lst
                newLst.append(left)
                newLst.append(right)
                return newLst

            # sum is smaller than target, increase the left pointer
            elif sum < target:
                left += 1

            # sum is larger than target, decrease the right pointer
            else:
                right -= 1


        return newLst