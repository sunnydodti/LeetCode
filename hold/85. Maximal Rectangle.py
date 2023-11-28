class Solution:
    def get_max(self, arr: list) -> int:
        if len(arr) == 1:
            return int(arr[0])
        if len(arr) == 2:
            return int(min(arr)) * 2
        areas = []
        for i in range(1, len(arr)):
            if arr[i] != "0" and arr[i-1] != "0":
                areas.append(int(arr[i-1]) * int(arr[i]))
        # print(areas)
        if areas:
            return max(areas)
        return 0

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if len(matrix) == 1:
            return self.get_max(matrix[0])

        l = len(matrix[0])
        # print(matrix[0])
        max = 0
        for i in range(1, len(matrix)):
            for j in range(l):
                # # print("\t",  matrix[i][j], matrix[i-1][j])
                if matrix[i][j] != "0" and matrix[i-1][j] != "0":
                    matrix[i][j] = str(int(matrix[i-1][j]) + 1)
                    # # print("\t\t",  matrix[i][j])
            a = self.get_max(matrix[i])
            max = a if a > max else max

            # print(matrix[i])
        return max
        # for i in matrix:
        #     for j in range(1, l):
        #         if matrix[i][j] != "0" and matrix[i][j-1] != "0":
        #             matrix[i][j] = str(int(matrix[i][j-1]) + 1)
            # # print(matrix[i])


if __name__ == "__main__":
    inp = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    inp = [["0"]]
    inp = [["0", "0"]]
    s = Solution()
    # print(s.largestSubmatrix(inp))
    print(s.maximalRectangle(inp))
