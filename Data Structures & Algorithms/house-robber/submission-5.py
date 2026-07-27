class Solution:
    def rob(self, nums: List[int]) -> int:
        
                # rob1 = max money we can rob up to house i-2
        # rob2 = max money we can rob up to house i-1

        rob1, rob2 = 0, 0

        for num in nums:
            
            # At each house, we have two choices:
            
            # 1. Rob this house:
            #    → take current house value (num)
            #    → plus rob1 (which is i-2, since we must skip previous house)
            rob_current = num + rob1

            # 2. Skip this house:
            #    → just keep rob2 (best up to previous house)
            skip_current = rob2

            # Choose the better of the two options
            temp = max(rob_current, skip_current)

            # Now shift our variables forward:
            
            # rob1 becomes old rob2 (move window forward)
            rob1 = rob2

            # rob2 becomes the new best result
            rob2 = temp

        # rob2 holds the final answer (best across all houses)
        return rob2