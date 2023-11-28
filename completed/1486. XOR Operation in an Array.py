class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        ans = 0
        for  i in range(start, start+n*2, 2):
            ans ^= i 
            nums.append(i)
        print(nums)
        return ans
if __name__ == "__main__":
    S = Solution()
    n = 4
    start = 3
    print(S.xorOperation(n, start))