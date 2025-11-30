class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """accepted"""
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if count == 0:
                    continue
                return count

            count += 1
        return count

    def lengthOfLastWord2(self, s: str) -> int:
        """accepted"""
        s = s.strip()
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return count
            count += 1
        return count

    def lengthOfLastWord3(self, s: str) -> int:
        """accepted"""
        return len(s.split()[-1])

    def lengthOfLastWord4(self, s: str) -> int:
        """accepted"""
        count = 0
        index = len(s) - 1
        while index >= 0:
            if s[index] == " ":
                if count == 0:
                    index -= 1
                    continue
                return count
            index -= 1
            count += 1
        return count

    def lengthOfLastWord5(self, s: str) -> int:
        """accepted"""
        count = 0
        index = len(s) - 1
        while index >= 0:
            if s[index] != " ":
                index -= 1
                count += 1
                continue
            if count == 0:
                index -= 1
                continue
            return count
        return count


if __name__ == "__main__":
    S = Solution()
    inp = "Hello World"
    inp = "H"
    inp = "luffy is still joyboy"
    inp = "luffy is still joyboy  "
    print(S.lengthOfLastWord(inp))
    print(S.lengthOfLastWord2(inp))
    print(S.lengthOfLastWord3(inp))
    print(S.lengthOfLastWord4(inp))
    print(S.lengthOfLastWord5(inp))
