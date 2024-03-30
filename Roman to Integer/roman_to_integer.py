class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        final=0
        prev=0
        for i in s:
            for k,v in roman_values.items():
                if(i==k and v>prev and prev!=0):
                    final=final-prev
                    final+=(v-prev) 
                    prev=v
                elif(i==k):
                    final+=v
                    prev=v
        return final