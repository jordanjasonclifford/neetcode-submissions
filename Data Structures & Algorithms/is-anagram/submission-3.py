class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if lengths of s and t not the same
        if len(s) != len(t):
            return False

        stMap = {}

        # add everything from s
        for i in s:
            if i in stMap:
                stMap[i] += 1
            else:
                stMap[i] = 1
        
        # check if everything in t is in s
        for i in t:
            if i not in stMap:
                return False
            stMap[i] -= 1   # auto subtract

            if stMap[i] < 0: # if something is in s more than t
                return False

        return True