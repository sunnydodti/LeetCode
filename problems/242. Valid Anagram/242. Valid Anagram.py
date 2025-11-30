from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """accepted"""
        return True if sorted(s) == sorted(t) else False

    def isAnagram2(self, s: str, t: str) -> bool:
        """accepted"""
        def get_map(inp: str) -> Dict[str, int]:
            map = {}
            for i in inp:
                if i in map:
                    map[i] = map.get(i) + 1
                    continue
                map[i] = 1
            return map

        smap = get_map(s)
        tmap = get_map(t)

        print(smap)
        print(tmap)
        return smap == tmap


if __name__ == "__main__":
    S = Solution()
    inps = [
        ("nagaram", "anagram"),
    ]
    inp = inps[-1]
    print(S.isAnagram(inp[0], inp[1]))
