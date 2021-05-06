'''
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

time complexity: O(log2(n))
space complexity: O(log2(n))
'''

class Solution:
    def myPow1(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow1(x, -n)

        half = self.myPow1(x, n//2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow2(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow2(x, -n)
        if n % 2:
            return x * self.myPow2(x, n-1)
        return self.myPow2(x*x, n/2)

if __name__ == '__main__':
    x = 3
    n = -2
    o = Solution()
    print(o.myPow1(x, n))
    print(o.myPow2(x, n))