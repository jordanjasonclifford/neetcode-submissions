class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary that stores:
        # fruit type -> how many of that fruit are in the current window.
        count = defaultdict(int)

        # l is the left boundary of the sliding window.
        # total is the current window length.
        # res stores the largest valid window found.
        l, total, res = 0, 0, 0

        # r is the right boundary of the sliding window.
        # It expands one position at a time.
        for r in range(len(fruits)):

            # Add the fruit at index r to the current window.
            count[fruits[r]] += 1

            # Increase the current window size.
            total += 1

            # We are only allowed to have at most two fruit types.
            # If there are more than two distinct fruit types,
            # shrink the window from the left.
            while len(count) > 2:

                # Get the fruit type currently leaving the window.
                f = fruits[l]

                # Remove one occurrence of that fruit from the window.
                count[f] -= 1

                # The window is now one element smaller.
                total -= 1

                # Move the left boundary forward.
                l += 1

                # If no copies of this fruit remain in the window,
                # remove its key from the dictionary.
                if not count[f]:
                    count.pop(f)

            # At this point, the window contains at most two
            # distinct fruit types, so it is valid.
            res = max(res, total)

        # Return the longest valid window found.
        return res