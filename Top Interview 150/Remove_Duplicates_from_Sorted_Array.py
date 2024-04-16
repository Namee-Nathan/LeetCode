class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        stack=[]
        for i in range(len(nums)):
            if(nums[i] not in stack ):
                nums[j]=nums[i]
                j+=1
                stack.append(nums[i])
            
        return j