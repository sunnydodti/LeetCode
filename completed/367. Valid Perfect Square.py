class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        from math import sqrt
        sq_root = str(sqrt(num))
        a,b = sq_root.split('.')
        print(a, ' - ', b)

        if int(b) > 0:
            return False
        return True
    
    def isPerfectSquare2(self, num: int) -> bool:
        from math import sqrt
        sq_root = sqrt(num)

        return sq_root.is_integer()
    
    def isPerfectSquare3(self, num: int) -> bool:
        n = 0

        while n*n <= num:
            if n*n == num:
                return True
            n += 1

        return False
    
    def isPerfectSquare4(self, num: int) -> bool:
        l, r = 0, n

        while l <= r:
            print(num, f'checking {l},{r} = ', end='')
            mid = (l+r) // 2

            print(mid)

            if mid*mid == num: return True
            sqr = mid*mid

            if sqr < num: l=mid+1
            if sqr > num: r=mid-1

        return False

if __name__ == "__main__":
    S = Solution()
    n = 1
    print(S.isPerfectSquare4(n))