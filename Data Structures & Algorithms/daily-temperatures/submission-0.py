class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1

            while j < n:
                if temperatures[j] > temperatures[i]:
                    break

                j += 1
                count += 1

            if j == n:
                count = 0
            

            res.append(count)

        return res