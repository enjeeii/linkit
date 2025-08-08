import random

class Mat:
    def __init__(self, m, n) -> None:
        self.row = m + 1
        self.col = n + 1
        self.data = [[0 for _ in range(n+2)] for _ in range(m+2)]

    def suffle(self):
        p1_x = random.randint(1, self.col)
        p1_y = random.randint(1, self.row)
        p2_x = random.randint(1, self.col)
        p2_y = random.randint(1, self.row)
        self.data[p2_y][p2_x] = 'T'
        self.data[p1_y][p1_x] = 'T'
    
    def __str__(self) -> str:
        res = ""
        for i in range(self.row):
            for j in range(self.col):
                res += str(self.data[i][j]) + " "
            res += "\n"
        return res

if __name__ == "__main__":
    mat = Mat(6, 8)
    mat.suffle()
    print(mat)
