class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack =[]
        res =[]
        def backtrack(o,c):
            if o == n and c== n:
                res.append("".join(stack))
                return
            if o < n:
                stack.append("(")
                backtrack(o+1,c)
                stack.pop()
            if c<o:
                stack.append(")")
                backtrack(o,c+1)
                stack.pop()
        backtrack(0,0)
        return res
        