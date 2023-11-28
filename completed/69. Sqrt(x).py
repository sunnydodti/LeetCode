class Solution:
    def mySqrt(self, x: int) -> int:
        print(x)
        l, r = 0, x//2 + 1

        while x:
            res, ans = self.isPerfectSquare4(x)
            if res:
                return ans
            x -= 1 
        

    def isPerfectSquare4(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            print(num, f'checking {l},{r} = ', end='')
            mid = (l+r) // 2

            print(mid)

            if mid*mid == num: return True, mid
            sqr = mid*mid

            if sqr < num: l=mid+1
            if sqr > num: r=mid-1

        return False, 0

if __name__ == '__main__':
    S = Solution()
    num = 0
    print(S.mySqrt(num))