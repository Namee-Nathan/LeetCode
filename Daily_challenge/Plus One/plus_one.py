class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        output=[]
        for i in digits:
           s+=str(i)
        out=int(s)+1
        for i in str(out):
            output.append(int(i))
        return output