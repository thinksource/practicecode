
class Node:

    def __init__(self, rootid)
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.rootid = value

    def getNodeValue(self):
        return self.rootid


class Solution:

    def longestConnsecutive(self, root):
        if root == None:
            return 0
        else:
            helper()

    def helper(self, treenode, curlen, lastvalue):
        if(treenode == None):
            return curlen
        elif treenode == lastValue + 1:
            curlen += 1
        else:
            curlen = 1
        left = helper(root.left, curLen, root.val)
        right = helper(root.right, curLen, root.val)
        return Math.max(Math.max(left, right), curLen)
