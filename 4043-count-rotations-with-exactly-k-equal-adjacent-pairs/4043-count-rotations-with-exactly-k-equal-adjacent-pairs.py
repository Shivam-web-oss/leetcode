class Solution(object):
    def countRotations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n= len(s)
        a=0
        for i in range(n):
            r=s[i:]+s[:i]
            sc=0
            for j in range(n-1):
                if r[j]== r[j+1]:
                    sc=sc+1
            if sc==k:
                a+=1
        return a
        