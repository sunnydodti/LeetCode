import string
from typing import Dict, Union


class Solution:
    def convertToTitle(self, columnNumber: int) -> Union[str, None]:
        """hold"""

        map: Dict[int, str] = {}
        ans = columnNumber % 26
        res = ""

        for i, letter in enumerate(string.ascii_uppercase):
            map[i+1] = letter
        count = 0

        def get_base26_number(num: int):
            return map.get(num)

        while columnNumber > 0:
            columnNumber = columnNumber // 26
            print("column", columnNumber)
            count += 1
            if columnNumber < 26:
            if columnNumber >= 26:
                res = get_base26_number(columnNumber) + res
            print(res)
        print("count", count)
        return res

    def convertToTitle(self, columnNumber: int) -> Union[str, None]:

        map: Dict[int, str] = {}

        for i, letter in enumerate(string.ascii_uppercase):
            map[i+1] = letter
        count = 0
        ans = [""]
        index = 1
        num = 0
        while columnNumber > 0:
            columnNumber -= 26
            if columnNumber > 0:
                count += 1
            if count <= 26:
                ans[index] = map.get(count)
            if count > 26:

        return res


if __name__ == "__main__":
    S = Solution()
    inp = 7+26
    inp = 701
    print(S.convertToTitle(inp))
