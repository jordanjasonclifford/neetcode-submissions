class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

         # dictionary to map sorted word -> list of anagrams
        groups = defaultdict(list)

        for word in strs:
            # sort the word so all anagrams share the same key
            # e.g. "eat", "tea", "ate" -> "aet"
            key = ''.join(sorted(word))
            
            # add the original word to the correct group
            groups[key].append(word)

        # return all grouped anagrams as a list
        return list(groups.values())



 