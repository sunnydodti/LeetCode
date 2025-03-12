class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        index_map: dict[int: int] = {}
        count_map: dict[int: int] = {}

        length: int = len(arr1)
        swap_index: int = length - 1

        for i, val in enumerate(arr2):
            index_map[val] = i
            count_map[val] = 0

        for i in range(len(arr2)):
            print(arr1[i], index_map.get(arr1[i]))
            if (not index_map.get(arr1[i])):
                if swap_index <= i:
                    continue
                


if __name__ == '__main__':
    solution = Solution()
    input1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    input2 = [2, 1, 4, 3, 9, 6]
    print(solution.relativeSortArray(input1, input2))
