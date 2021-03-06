class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n = len(matrix)
        m = len(matrix[0])
        self.sums = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n):
            for j in range(1, m):
                self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] + self.matrix[i-1][j-1] - self.sums[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)