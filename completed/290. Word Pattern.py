class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """accepted"""
        words = s.split()
        print(words)
        print(len(words), len(pattern), len(words) == len(pattern))
        if len(words) != len(pattern):
            return False
        map = {}
        word_map = {}
        for i in range(len(pattern)):
            if pattern[i] in map:
                if map.get(pattern[i]) != words[i]:
                    return False
                continue
            if word_map.get(words[i]):
                return False
            map[pattern[i]] = words[i]
            word_map[words[i]] = True
        return True


if __name__ == "__main__":
    S = Solution()
    inps = [
        ("abba", "dog dog dog dog"),
        ("abba", "dog cat cat dog"),
    ]

    inp = inps[-1]
    print(S.wordPattern(inp[0], inp[1]))
