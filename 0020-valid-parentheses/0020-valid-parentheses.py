class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        bracketMap={')':'(','}':'{',']':'['}
        for char in s:
            if char in bracketMap:
                # top=stack.pop() if stack else '#'
                # if bracketMap[char] != top:
                #     return False
                if not  stack or stack.pop()!=bracketMap[char]:
                    return False
            else:
                stack.append(char)
        return not stack        