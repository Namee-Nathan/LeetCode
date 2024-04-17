class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        stack=[]
        if(nums==[]):
            return 0
        else:
            for n in range(len(nums)):
                if(stack.count(nums[n])<=1):
                    nums[j]=nums[n]
                    stack.append(nums[n])
                    j+=1
        return(j)