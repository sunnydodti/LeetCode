class SubrectangleQueries:

    _rectangle = []

    def __init__(self, rectangle: list[list[int]]):
        self._rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        print("-"*20)
        print(row1, col1, row2, col2)
        for i in range(row1, row2+1):
            # print(i)
            for j in range(col1, col2+1):
                # print(f"\t{j}")
                print("\t\t", i, j)
                self._rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return (self._rectangle[row][col])
        pass
        # Your SubrectangleQueries object will be instantiated and called as such:
        # obj = SubrectangleQueries(rectangle)
        # obj.updateSubrectangle(row1,col1,row2,col2,newValue)
        # param_2 = obj.getValue(row,col)

    def display(self):
        for i in self._rectangle:
            print(i)


if __name__ == "__main__":

    inp = [
        [
            [1, 2, 1],
            [4, 3, 4],
            [3, 2, 1],
            [1, 1, 1]
        ],
        [0, 2],
        [0, 0, 3, 2, 5],
        [0, 2],
        [3, 1],
        [3, 0, 3, 2, 10],
        [3, 1],
        [0, 2]
    ]

    s = SubrectangleQueries(inp[0])
    s.display()
    print(s.getValue(inp[1][0], inp[1][1]))
    print(inp[2])
    s.updateSubrectangle(inp[2][0], inp[2][1], inp[2][2], inp[2][3], inp[2][4])
    s.display()
    print(s.getValue(inp[3][0], inp[3][1]))
    print(s.getValue(inp[4][0], inp[4][1]))
    s.updateSubrectangle(inp[5][0], inp[5][1], inp[5][2], inp[5][3], inp[5][4])
    s.display()
    print(s.getValue(inp[6][0], inp[6][1]))
