class Solution:

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results

//the java solution
class jSolution:

    def subsets(self, nums):
        ret = []
        if(len(nums) == 0):
            return ret
        list = []
        self.dfs(ret, list, sorted(nums),0)
        return ret

    def dfs(self, ret, list, S, index):
        ret.append(list.copy())

        for i in range(index, len(S)):
            list.append(S[i])
            # print(list)
            self.dfs(ret, list,S, i+1)
            del list[-1]

// Non Recursion
class NRSolution:

    def subsets(self, nums):
        ret=[]
        l = len(nums)
        for i in range(0, 1 <<l):
            subset=[]
            for j in range(0, l):
                if (i & 1 << j != 0):
                    subset.append(nums[j]);
            ret.append(subset.copy())
        return ret
