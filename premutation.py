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

class jSolution:

    def subsets(self, nums):
        ret=[]
        if(len(nums) == 0):
            return ret
        list=[]
        self.dfs(ret, list, sorted(nums),0)
        return ret

    def dfs(self, ret, list, S, index):
        ret.append(list.copy())

        for i in range(index, len(S)):
            list.append(S[i])
            # print(list)
            self.dfs(ret, list,S, i+1)
            del list[-1]
