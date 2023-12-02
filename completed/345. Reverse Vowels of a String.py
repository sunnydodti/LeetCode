class Solution:
    def reverseVowels(self, s: str) -> str:
        """accepted"""
        s = list(s)
        vovels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        i, j = 0, len(s)-1
        while i <= j:
            print(s[i], s[j])
            if s[i] not in vovels:
                i += 1
                continue
            if s[j] not in vovels:
                j -= 1
                continue

            # if s[i] in vovels and s[j] in vovels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)

if __name__ == "__main__":
    S = Solution()
    inp = "hello"
    inp = "leotcede"
    inp = "lwlwlwl"
    inp = "aoaoaoao"
    inp = "a"
    inp = "p"
    print(S.reverseVowels(inp))
