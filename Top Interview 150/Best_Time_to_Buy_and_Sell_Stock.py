class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev_low=-1
        prev_high=0
        profit=0
        for i in prices:
            if(i<prev_low or prev_low==-1):
                prev_low=i
                prev_high=0
            elif(i>prev_high):
                prev_high=i
            if(prev_high-prev_low>0 and prev_high-prev_low>profit):
                profit=prev_high-prev_low
        if(profit) >0:
            return profit
        else:
            return 0