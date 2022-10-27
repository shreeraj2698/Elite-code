class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        n = str(bin(n)) 
        for i in range(len(n)):
            if n[i] == "1" :
                count += 1
        return count
        