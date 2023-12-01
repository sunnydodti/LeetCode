class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """wrong"""
        def get_unique_letters(word: str) -> str:
            letters = []

            for letter in word:
                if letter not in letters:
                    letters.append(letter)

            return "".join(letters)
        s_letters = get_unique_letters(s)
        t_letters = get_unique_letters(t)

        if len(s_letters) != len(t_letters):
            return False
        print(s_letters)
        print(t_letters)
        for i in range(len(t_letters)):

            print(t_letters[i], s_letters[i])
            print("\t", t)
            t = t.replace(t_letters[i], s_letters[i])
            print("\t", t)
        print(s)
        print(t)
        return s == t

    def isIsomorphic2(self, s: str, t: str) -> bool:
        """wrong"""
        def get_unique_letters(word: str) -> str:
            letters = []

            for letter in word:
                if letter not in letters:
                    letters.append(letter)

            return "".join(letters)
        s_letters = get_unique_letters(s)
        t_letters = get_unique_letters(t)

        if len(s_letters) != len(t_letters):
            return False
        print(s_letters)
        print(t_letters)
        letters = sorted(s_letters, reverse=True)
        map = {key: t_letters[i] for i, key in enumerate(s_letters)}
        print(map)
        for letter in letters:
            print(map.get(letter), letter)
            print("\t", t)
            t = t.replace(map.get(letter), letter)
            print("\t", t)
        print(s)
        print(t)
        return s == t

    def isIsomorphic3(self, s: str, t: str) -> bool:
        """accepted"""
        map = {}

        for i in range(len(s)):
            print(s[i], t[i])
            if s[i] in map:
                if map.get(s[i]) != t[i]:
                    print(f"\{map.get(s[i])}, {t[i]}")
                    print(f"\tduplicate mapping")
                    return False
                continue
            # print(map.values())
            if t[i] in map.values():
                print(f"\t{t[i]} - {map.values()}")
                print(f"\tduplicate mapping")
                return False
            map[s[i]] = t[i]
            print(map)
        # if len(set(map.values())) != len(map):
        #     return False
        return True


if __name__ == "__main__":
    S = Solution()
    s = "paper"
    t = "title"
    # s = "bbbaaaba" # True
    # t = "bbbaaaba"
    # s = "abab" # True
    # t = "baba"
    s = "badc"  # False
    t = "baba"
    s = "egg"  # True
    t = "add"
    # print(S.isIsomorphic(s, t))
    # print(S.isIsomorphic2(s, t))
    print(S.isIsomorphic3(s, t))
