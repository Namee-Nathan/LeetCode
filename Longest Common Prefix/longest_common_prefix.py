class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        final_length=0
        exit_flag=True
        len_itr=min(len(s) for s in strs)
        if(len_itr==1 and len(strs)==1):
            return strs[0][0]
        else:
            for i in range(1,len(strs)):
                first=strs[0]
                it_str=""
                lenth=0
                for j in range(0,len_itr):
                    
                    if(first[j]==strs[i][j]):
                        it_str+=first[j]
                        lenth=j
                    elif(first[0]!=strs[i][0]):
                        exit_flag=False
                        break
                    else:
                        break
                if(final_length==0):
                    final_length=lenth
                    result=it_str
                elif(final_length>lenth):
                    result=it_str
                    final_length-lenth
            if(exit_flag!=False):
                return result 
            else:
                return ""