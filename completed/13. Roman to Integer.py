class Solution:
    def romanToInt(self, s: str) -> int:
        """accepted"""
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        l = len(s)
        sum = 0
        for i in range(l):
            if i < l-1 and map[s[i]] < map[s[i+1]]:
                sum = sum - map[s[i]]
                continue
            sum += map[s[i]]
        return sum
        
if __name__ == "__main__":
    S = Solution()
    inp = "LIVIII"
    inp = "IVIII"
    inp = "C"
    print(S.romanToInt(inp))
