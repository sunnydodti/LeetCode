class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I':   1,
            'V':   5,
            'X':   10,
            'L':   50,
            'D':   100,
            'M':   500,
            'M':   1000
        }

        num = 0
        skip_condition = False

        for i in range(len(s)):
            if skip_condition:
                continue
            num += map[s[i]]

        return num


if __name__ == "__main__":
    solution = Solution()
    inp = 'LVIII'
    print(solution.romanToInt(inp))
