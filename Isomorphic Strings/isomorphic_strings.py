class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n=len(set(s))
        m=len(set(t))
        z=len(set(zip(s,t)))
        return n==m==z