class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False

        sety = set()

        for x in nums:
            if x in sety:
                return True

            sety.add(x)

        return False
 
            