class Solution:
    def isHappy(self, n: int, checked_numbers:list[int] = []) -> bool:
        used = []

        if checked_numbers:
            used = checked_numbers
        print(n, used, '-- checked numbers')

        if n in used:
            return False
        used.append(n)        
        new = 0

        while n:
            a = (n % 10)
            new += a**2
            n = n//10

            print(a, '->', a**2)
        print('sum = ', new)

        if new == 1:
            return True

        if (new > 1):
            return self.isHappy(new, used)
        print('sum -- ', new)

        return False


if __name__ == "__main__":
    S = Solution()
    print(S.isHappy(1111111))
