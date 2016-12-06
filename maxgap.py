class Bucket:
    def __init__(self):
        self.valid=False

    def add(self, n):
        if (!self.valid):
            self.nMin=n
            self.nMax=n
            valid= True
        else:
            if(self.nMax<n):
                self.nMax=n
            elif self.nMin>n:
                self.nMin= n

def CalcMaxGap(a):
    l=len(a)
    b=[]
    nMax=a[0]
    nMin=a[0]
    for i in range(l):
        b.append(Bucket())
    for i in a:
        if nMax<i:
            nMax=i
        elif nMin > i:
            nMin = i
    delta=nMax-nMin
    for i in range(l):
        nBucket=(a[i]-nMin)*l/delta
        if nBucket>=l:
            nBucket=l-1
        b[nBucket].add(a[i])

    i=0
    nGap=delta/l
    for j range(1, l):
        if b[j].valid:
            gap=b[j].nMin-p[i].nMax
            if nGap<gap:
                nGap=gap
            i=j
    return nGap
