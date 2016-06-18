import math
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end=start, end
        self.left,self.right=None, None


class SegmentTree:

    def build(self,start, end):
        node=new SegmentTreeNode(start, end)
        if(start!=end):
            firstend=math.floor((start + end) / 2)
            node.left=self.build(start,firstend)
            node.right=self.build(firstend+1, end)
        return node
