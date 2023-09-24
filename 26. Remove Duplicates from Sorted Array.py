class Solution(object):
    def removeDuplicates(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        for i,n  in enumerate (nums):

            if nums.count(n)>1:
                for i in range (nums.count(n)-1):

                    nums.remove(n)
                
    