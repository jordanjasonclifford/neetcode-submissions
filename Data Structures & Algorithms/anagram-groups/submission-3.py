class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
         # Maps each sorted-letter pattern to the words
        # that produce that same pattern.
        #
        # Example:
        # "eat", "tea", and "ate" all produce the key "aet".
        groups = defaultdict(list)

        # Examine each word in the input list.
        for word in strs:
            # Sort the letters so that all anagrams share
            # the same normalized representation.
            #
            # sorted("tea") returns ['a', 'e', 't']
            # "".join(...) converts it back into "aet".
            key = "".join(sorted(word))

            # Add the original word to the list associated
            # with its sorted-letter key.
            groups[key].append(word)

        # The problem only wants the groups of original words,
        # not the sorted keys used internally.
        return list(groups.values())

        
