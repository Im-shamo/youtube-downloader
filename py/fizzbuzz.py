class Solution:
    def fizzBuzz(self, n):
        ans=list()
        for i in range(1, n+1):
            a = ""
            if i % 3 == 0: a += "fizz"
            if i % 5 == 0: a += "buzz"
            
            if a == "": a += str(i)
            ans.append(a)
        return ans
    
    def countBits(self, n: int):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
print(Solution().countBits(100))
