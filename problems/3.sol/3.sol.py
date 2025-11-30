class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        length = 0

        char_set = set()

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            length = max(length, end - start + 1)
        return length


if __name__ == "__main__":
    S = Solution()
    # print(S.lengthOfLongestSubstring("abcabcbb"))
    print(S.lengthOfLongestSubstring("pwwkew"))
