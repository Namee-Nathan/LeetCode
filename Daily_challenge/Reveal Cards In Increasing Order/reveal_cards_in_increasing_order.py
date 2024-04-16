class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        ans=[]
        deck.sort(reverse=True)
        for i in deck:
            ans=[i]+ans[-1:]+ans[:-1]
            print(i)
            print(ans)
        return ans 