import operator
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
    	value_count={}
    	for i in num:
    		t=i
    		if (i+1 in value_count or i-1 in value_count) and (not i in value_count):
    			m=i
    			if (i+1 in value_count and i-1 in value_count):
    				value_count[i-1] += value_count[i+1]
    				value_count[i+1] = value_count[i-1]
    			while t + 1 in value_count:
    				value_count[t + 1] += 1
    				if t in value_count:
    					value_count[t + 1]=value_count[t]
    				t += 1
    			while m - 1 in value_count:
    				value_count[m - 1] += 1
    				if m in value_count:
    					value_count[m - 1]=value_count[m]
    				m -= 1
    			if i+1 in value_count:
    				value_count[i]=value_count[i + 1]
    			if i-1 in value_count:
    				value_count[i]=value_count[i - 1]
    		if not i in value_count:
    			value_count[i] = 1
        return value_count[max(value_count, key=value_count.get)]
