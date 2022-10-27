from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = defaultdict()
        for i in range(len(nums)):
            if(nums[i] not in a ):
                a[nums[i]] = 1
            elif (a.get(nums[i])!=None):
                a[nums[i]] = int(a.get(nums[i]))+1
        return a.keys()[a.values().index(1)]

            