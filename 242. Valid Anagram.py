class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """accepted"""
        return True if sorted(s) == sorted(t) else False


if __name__ == "__main__":
    S = Solution()
    inps = [
        ("nagaram", "anagram"),
    ]
    inp = inps[0]
    print(S.isAnagram(inp[0], inp[1]))
