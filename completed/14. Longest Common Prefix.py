from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """accepted"""
        common_prefix = ""
        l = min([len(word) for word in strs])
        for i in range(l):
            letter = strs[0][i]
            is_valid = True
            for word in strs:
                if word[i] != letter:
                    is_valid = False
                    break
            if not is_valid:
                return common_prefix
            common_prefix += letter
        return common_prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """accepted"""
        common_prefix = ""
        strs.sort()
        print(strs)
        a = strs[0]
        b = strs[-1]

        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                return common_prefix
            common_prefix += a[i]
        return common_prefix


if __name__ == "__main__":
    S = Solution()
    inp = ["flower", "flow", "flight"]
    inp = ["f", "a", "f"]
    inp = ["flower"]
    inp = ["flower"]*9
    inp = ["flower", "f"]*9
    print(S.longestCommonPrefix2(inp))
