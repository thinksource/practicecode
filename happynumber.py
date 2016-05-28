class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        numset=set()
        while True:
            sum = 0
            while (n != 0):
                k = n % 10
                sum += k ** 2
                n = n // 10
            if sum == 1:
                return True
            elif sum in numset:
                return False
            else:
                numset.add(sum)
