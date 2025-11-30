class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)]
        j, d = 0, 1

        for i in range(len(s)):
            rows[j] += s[i]
            print(j, rows, s[i], ' ', end='')
            if j == numRows-1:
                d = -1
            elif j == 0:
                d = 1
            print(d, ' ', end='')
            j += d
            print(j)

        print(rows)
        return ''.join(rows)


if __name__ == '__main__':
    C = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(C.convert(s, numRows))
