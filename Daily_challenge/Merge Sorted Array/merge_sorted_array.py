class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        def find_index(e):
            for i in range(0,len(nums1)):
                if(nums1[i]>=e):
                    return i
        new_list=nums1[:m]+nums2[:n]
        nums1=nums1[:m]
        print(new_list)
        prev=0
        for i in new_list:
            if(i<prev):
                j=find_index(i)
                nums1[j:j]=[i]
                prev=i
            elif(i>prev and i not in nums1):
                nums1.append(i)
                prev=i
            else:
                prev=i
            


    
s=Solution()
s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)