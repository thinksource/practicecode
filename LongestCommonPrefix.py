# this is for the problem http://www.lintcode.com/en/problem/longest-common-prefix/
class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        common=""
        if len(strs) == 0 :
            return common
        if len(strs) == 1 :
            return strs[0]

        first=strs[0]

        for j in range(0, len(first)):

            for i in range(1,len(strs)):
                if len(strs[i]) <= j:
                    return common
                if(first[j] != strs[i][j]):
                    return common
            common+=first[j]
        return common
