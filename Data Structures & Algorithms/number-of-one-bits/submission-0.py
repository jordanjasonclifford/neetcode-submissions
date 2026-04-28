class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0  # this will count how many 1 bits we see

        # keep looping until n becomes 0 (no more bits left to check)
        while n:

            # n & 1 checks the LAST (rightmost) bit
            # if last bit is 1 → (n & 1) = 1
            # if last bit is 0 → (n & 1) = 0
            if n & 1:
                res += 1  # count the 1 bit

            # shift all bits to the right by 1
            # this "removes" the last bit we just checked
            # example: 1011 → 0101 → 0010 → 0001 → 0000
            n >>= 1

        return res