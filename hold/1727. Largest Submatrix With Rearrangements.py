class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        """wrong"""
        count = len([1 for i in matrix for j in i if j == 1])
        print(count)

        ans = 1
        while True:
            if (ans**2) > count:
                return (ans - 1) ** 2
            ans += 1

    def largestSubmatrix2(self, matrix: list[list[int]]) -> int:
        """work in progress"""
        lengths = []
        heights = []
        for row in matrix:
            lengths.append(row.count(1))
            # print("\t", n)
            # row.sort(reverse=True)

            print(row)
        print(lengths, heights)

        # print(m, n, m*n)


if __name__ == "__main__":
    inp = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]

    s = Solution()
    # print(s.largestSubmatrix(inp))
    print(s.largestSubmatrix2(inp))
