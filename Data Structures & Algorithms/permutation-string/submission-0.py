class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # build frequency map for s1
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)  # number of unique chars we need to match

        # try every starting index in s2
        for i in range(len(s2)):
            count2 = {}     # frequency map for current substring
            curr = 0        # how many chars currently match required frequency

            # expand substring starting at i
            for j in range(i, len(s2)):

                # add current char to window
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                # if we exceed required frequency → invalid, stop early
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break

                # if this char now matches exactly what we need
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    curr += 1

                # if all characters match → permutation found
                if curr == need:
                    return True

        return False

        