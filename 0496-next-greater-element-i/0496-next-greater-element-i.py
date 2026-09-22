class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n={}
        s=[]
        for num in nums2:
            while s and s[-1]<num:
                n[s.pop()]=num
            s.append(num)
        return [n.get(x,-1) for x in nums1]