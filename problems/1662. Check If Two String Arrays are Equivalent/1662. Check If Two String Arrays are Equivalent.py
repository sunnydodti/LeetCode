from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """accepted"""
        return "".join(word1) == "".join(word2)

    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        """accepted"""
        a = ""
        for word in word1:
            a += word
        b = ""
        for word in word2:
            print(word)
            b += word
            print("\t", b, a, b in a)
            if b not in a:
                return False
        return a == b


if __name__ == "__main__":
    S = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    word1 = []
    word2 = []
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(S.arrayStringsAreEqual(word1, word2))
    print(S.arrayStringsAreEqual2(word1, word2))
