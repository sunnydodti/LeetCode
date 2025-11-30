
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """accepted"""
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        """accepted"""
        ans = -1
        for i in range(len(haystack)-len(needle)+1):
            match = ""
            index = -1
            print(f"{haystack[i]} == {needle[0]} {haystack[i] == needle[0]}")
            if haystack[i] == needle[0]:
                index = i
                count = index
                is_valid = True
                for j in range(1, len(needle)):
                    count += 1
                    print(
                        f"\t{haystack[count]} == {needle[j]} {haystack[count] == needle[j]}")
                    if haystack[count] != needle[j]:
                        is_valid = False
                        break

                if not is_valid:
                    continue
                return index
            print(i)
        return ans


if __name__ == "__main__":
    S = Solution()
    inp1, inp2 = "satdbutsad", "sad"
    inp1, inp2 = "sd a d", "a "
    # print(S.strStr(inp1, inp2))
    print(S.strStr2(inp1, inp2))
