class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_num=0
        output_list=[]
        # build the hash table
        new_list=nums[:]
        # Find the complement
        while True:
            j=nums[0]
            for i in range(1,len(nums)):
                if(nums[i]+j==target):
                    output_list.extend([new_list.index(j),new_list.index(nums[i],new_list.index(j)+1)])
                    break
            if(output_list==[]):
                nums.remove(j)
            else:
                break
        # return the final list
        return output_list
