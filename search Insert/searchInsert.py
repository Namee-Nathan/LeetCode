class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        last=0
        for i in range(0,len(nums)):
            if(nums[i]==target):
                last=i
                break
            elif(nums[i]>target):
                last=i
                break
            else:
                last=i+1
        return last

