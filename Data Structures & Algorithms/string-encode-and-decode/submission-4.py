class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""  # final encoded string

        # loop through each string
        for s in strs:
            # store: length of string + '#' + the string itself
            # example: "cat" -> "3#cat"
            res += str(len(s)) + "#" + s

        return res


    def decode(self, s: str) -> List[str]:

        res = []  # list to store decoded strings
        i = 0     # pointer to walk through the string

        # keep going until we reach the end of encoded string
        while i < len(s):

            j = i  # j will find the '#' delimiter

            # move j until we hit '#'
            while s[j] != "#":
                j += 1

            # substring from i to j is the length (as string)
            # convert it to int
            length = int(s[i:j])

            # extract the actual word:
            # starts after '#' → j+1
            # ends at j+1+length
            res.append(s[j + 1 : j + 1 + length])

            # move i to the start of the next encoded word
            i = j + 1 + length

        return res