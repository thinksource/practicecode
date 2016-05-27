class Solution:
    def triangleCount(self, S):
        edges = sorted(S)
        ans=0
        for i in range(len(edges)):
            left=0
            right=i-1;
            while(left<right):
                if(edges[left]+edges[right]>edges[i]):
                    ans+=right-left
                    right-=1
                else:
                    left+=1
        return ans
