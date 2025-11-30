class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m-1, -1, -1):
            print(grid[i])
            if grid[i][-1] > -1:
                break
            for j in range(n-1, -1, -1):
                print('\t', grid[i][j], end = ' : ')
                if grid[i][j] > -1:
                    break
                count += 1
                print(count)
            print('')
        return count
        
if __name__ == '__main__':
    S = Solution()
    inp = [
            [4,3,2,-1],
            [3,2,1,-1],
            [1,1,-1,-2],
            [-1,-1,-2,-3]
            ]
    print(S.countNegatives(inp))