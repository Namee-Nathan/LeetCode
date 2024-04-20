class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True  

        #Start at num[-2] since nums[-1] is given
        backtrack_index = len(nums)-2 
        #At nums[-2] we only need to jump 1 to get to nums[-1]
        jump =1  

        while backtrack_index>0:
            #We can get to the nearest lily pad
            if nums[backtrack_index]>=jump: 
                #now we have a new nearest lily pad
                jump=1 
            else:
                #Else the jump is one bigger than before
                jump+=1 
            backtrack_index-=1
        
        #Now that we know the nearest jump to nums[0], we can finish
        if jump <=nums[0]: 
            return True
        else:
            return False 