from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                a.remove(i)
        return a.pop()

            