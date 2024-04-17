class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in range(len(nums)):
            if(nums[i] in count):
                count[nums[i]]+=1
            else:
                count[nums[i]]=1
        for k,v in count.items():
            if(v>len(nums)/2):
                return(k)
            