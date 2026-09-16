class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_con=0
        c_con=0
        for num in nums:
            if num ==1:
                c_con+=1
            else:
                m_con = max(m_con,c_con)
                c_con =0
        return max(m_con,c_con)
        