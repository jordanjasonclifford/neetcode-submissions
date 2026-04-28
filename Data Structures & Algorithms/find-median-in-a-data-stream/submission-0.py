class MedianFinder:

    def __init__(self):
        # store all numbers
        self.data = []

    def addNum(self, num: int) -> None:
        # just append the number
        self.data.append(num)

    def findMedian(self) -> float:
        # sort the list so we can find the middle
        self.data.sort()

        n = len(self.data)

        # if n is odd (remainder when dividing by 2 is 1)
        if n % 2 == 1:
            # return the middle element
            return self.data[n // 2]

        # if n is even
        else:
            # average the two middle elements
            return (self.data[n // 2] + self.data[n // 2 - 1]) / 2