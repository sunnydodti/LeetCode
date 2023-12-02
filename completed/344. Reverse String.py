from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """accepted"""
        """
        Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]
        print("i", s)

    def reverseString2(self, s: List[str]) -> None:
        """accepted"""
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1

        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print("i", s)
    
    def reverseString3(self, s: List[str]) -> None:
        """accepted"""
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

if __name__ == "__main__":
    S = Solution()
    inp = ["H", "a", "n", "n", "a", "h"]
    inp = ["h", "e", "l", "l", "o"]
    og_inp = inp.copy()
    S.reverseString(inp)
    print("o", og_inp)
    print("r", inp)
    print(og_inp[::-1] == inp)
