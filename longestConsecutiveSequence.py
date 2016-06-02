import operator
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
    	nums_set=set()
        rmax=0
        for i in num:
            nums_set.add(i)
        for j in num:
            left=j-1
            right=j+1
            count=1
            while left in nums_set:
                count+=1
                nums_set.remove(left)
                left-=1
            while right in nums_set:
                count+=1
                nums_set.remove(right)
                right+=1
            rmax=max(rmax, count)
        return rmax
