class Solution:
    def firstUniqChar(self, s: str) -> int:
        """accepted"""
        count_map = {}
        index_map = {}
        index = -1
        for letter in s:
            print(letter, letter in count_map)
            index += 1
            if letter in count_map:
                print(f"\t {count_map.get(letter)} -> {count_map.get(letter) + 1}")
                count_map[letter] = count_map.get(letter) + 1
                continue
            count_map[letter] = 1
            index_map[letter] = index
        print(index_map)
        print(count_map)

        for letter in count_map:
            if count_map.get(letter) == 1:
                return index_map.get(letter)
        return -1

    def firstUniqChar2(self, s: str) -> int:
        """accepted"""
        count_map = {}
        l = len(s)
        for i in range(l):
            print(s[i], s[i] in count_map)
            if s[i] in count_map:
                print(f"\t {count_map.get(s[i])} -> {count_map.get(s[i]) + 1}")
                count_map[s[i]] = count_map.get(s[i]) + 1
                continue
            count_map[s[i]] = 1

        print(count_map)

        for i in range(l):
            if count_map.get(s[i]) == 1:
                return i
        return -1

    def firstUniqChar3(self, s: str) -> int:
        """accepted"""
        for i in s:
            if s.find(i) == s.rfind(i):
                return s.find(i)
        return -1


if __name__ == "__main__":
    S = Solution()
    inp = "l"
    inp = "leetcode"
    inp = "loveleetcode"
    print(S.firstUniqChar(inp))
    print(S.firstUniqChar2(inp))
    print(S.firstUniqChar3(inp))