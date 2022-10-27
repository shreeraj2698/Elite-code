import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list([])
        dup_free_set = []
        def all_possible(n):
            if(n<0):
                return;
            for i in itertools.combinations(nums, n):
                if sorted(list(i)) not in dup_free_set:
                    ans.append(i)
                    dup_free_set.append(sorted(i))
            all_possible(n-1)
        all_possible(len(nums))
        return list(set(ans))
        
        #******************backtracking************************
        # ans = []
        # currSet = []
        # def addSubset(currSet, nums, index):
        #     if(sorted(currSet) not in ans):
        #         ans.append(sorted(copy.deepcopy(currSet)))
        #     for i in range(index, len(nums)):
        #         if i != index and nums[i] == nums[i-1]:
        #             continue
        #         currSet.append(nums[i])
        #         addSubset(currSet, nums, i+1)
        #         currSet.pop()
        # sorted(nums)
        # addSubset(currSet, nums, 0)
        # return sorted(ans);
            