class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        l = len(mat)
        start = 0
        end = l-1
        sum = 0

        for i in range(l):
            line = mat[i]
            # print(line)

            if start == end:
                sum += line[start]

                start += 1
                end -= 1
                continue

            # print(f'{start} {end}')
            # print(f'{line[start]} {line[end]}')

            sum += line[start]
            sum += line[end]


            start += 1
            end -= 1
        return sum
    
    def diagonalSum2(self, mat: list[list[int]]) -> int:
        l = len(mat)
        start = 0
        end = l-1
        if l % 2 == 0:
            l -= 1 
        sum = 0

        for i in range(l//2 + 1):
            print(f'{i} ----{start}-{end}---------')

            if start == end:
                print(f'{mat[start][start]}')
                print()

                sum += mat[start][start]

                start += 1
                end -= 1
                continue

            print(f'{mat[start][start]} : {mat[start][end]} - {mat[end][start]} : {mat[end][end]}')
            
            sum += mat[start][start]
            sum += mat[start][end]
            sum += mat[end][start]
            sum += mat[end][end]

            start += 1
            end -= 1

        return sum

if __name__ == '__main__':
    S = Solution()
    inp = [[1,2,3],[4,5,6],[7,8,9]]    
    # inp = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    # inp = [[5]]
    print(S.diagonalSum2(inp))