class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}  # dictionary to store: number -> frequency

        # loop through each number in nums
        for num in nums:
            # if num already in dict, get its count, else start at 0
            # then add 1
            count[num] = count.get(num, 0) + 1

        # sort the keys of the dictionary based on their frequency (value)
        # count.get tells sorted() to use the frequency as the sorting key
        # reverse=True means highest frequency first
        sorted_nums = sorted(count, key=count.get, reverse=True)

        # return the first k elements (top k frequent numbers)
        return sorted_nums[:k]