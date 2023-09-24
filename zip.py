class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i, n in enumerate(nums):
            if nums.count(n)>2:

                for i in range (nums.count(n)-2):

                    nums.remove(n)
