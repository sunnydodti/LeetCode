class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        l = len(grid)
        x = 0
        y = len(grid[0])
        for i in range(l):
            for j in range(l):
                # print(f'[{i},{j}]:{grid[i][j]}', end = ' ')
                num = grid[i][j]
                print(i, j, ':', grid[i][j], end = ' - ')
                
                if i == j:
                    print('\\')
                    if num < 1:
                        return False
                    continue
                
                if (i+j) == (l - 1):
                    print(f'/ {i+j} = {l-1}')
                    if num < 1:
                        return False
                    continue
                
                print('')
                
                if num != 0:
                    return False 
            
            print('')
        print('---------')
        return True
        


if __name__ == '__main__':
    S = Solution()
    inp = [ [2,0,0,1],
            [0,3,1,0],
            [0,5,2,0],
            [4,0,0,2]]
    # inp = [ [5,7,0],
    #         [0,3,1],
    #         [0,5,0]]
    print(S.checkXMatrix(inp))