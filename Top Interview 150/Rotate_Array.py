class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=k%l
        i,j=0,l-k
        #partition
        k=j
        while(i<j and k!=l):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
                # when i reaches partiton , update partition value
                if(i==k and j!=l):
                    k=j
                # when j reaches the end,  update the value j to partition index
                elif(j>l-1):
                    j=k
       

            
        