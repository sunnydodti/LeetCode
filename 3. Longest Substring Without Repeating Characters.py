class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        length = 0

        character_map = {}
        print(s)

        for end, character in enumerate(s):

            if character in character_map:
                character_map[character] = end
                start = character_map[character]
            else:
                character_map[character] = end

            length = max(length, end - start + 1)
            print(character_map)

        return length

if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring("abcabcbb"))