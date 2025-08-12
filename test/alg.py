from operator import truediv
import random

MAT = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0],
    [0, 2, 2, 2, 2, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

def check(mat, source, target):
    def link_zero(source, target):
        if source[0] == target[0]:
            for i in range(min(source[1], target[1])+1, max(source[1], target[1])):
                if mat[source[0]][i] != 0:
                    return None
            return [(source[0], x) for x in range(min(source[1], target[1]), max(source[1], target[1])+1)]
        elif source[1] == target[1]:
            for i in range(min(source[0], target[0])+1, max(source[0], target[0])):
                if mat[i][source[1]] != 0:
                    return None
            return [(x, source[1]) for x in range(min(source[0], target[0]), max(source[0], target[0])+1)]
        else:
            return None
    
    def link_one(source, target):
        for p in [(source[0], target[1]), (target[0], source[1])]:
            line1 = link_zero(source, p)
            line2 = link_zero(p, target)
            if line1 is not None and line2 is not None:
                return line1 + line2
        return None


    def link_two(source, target):
        wait = []
        step = 1
        find = True
        while find:
            find = False
            if source[0]-step >= 0:
                if mat[source[0]-step][source[1]] == 0:
                    wait.append((source[0]-step, source[1]))
                    find = True
            if source[0]+step < len(mat):
                if mat[source[0]+step][source[1]] == 0:
                    wait.append((source[0]+step, source[1]))
                    find = True
            if source[1]-step >= 0:
                if mat[source[0]][source[1]-step] == 0:
                    wait.append((source[0], source[1]-step))
                    find = True
            if source[1]+step < len(mat[0]):
                if mat[source[0]][source[1]+step] == 0:
                    wait.append((source[0], source[1]+step))
                    find = True
            step += 1

        for p in wait:
            line1 = link_zero(source, p)
            line2 = link_one(p, target)
            if line1 is not None and line2 is not None:
                return line1 + line2
        return None
    
    line = link_zero(source, target)

    if line is not None:
        for p in line:
            if mat[p[0]][p[1]] == 0:
                mat[p[0]][p[1]] = 1
    else:
        line = link_one(source, target)
        if line is not None:
            for p in line:
                if mat[p[0]][p[1]] == 0:
                    mat[p[0]][p[1]] = 1
        else:
            line = link_two(source, target)
            if line is not None:
                for p in line:
                    if mat[p[0]][p[1]] == 0:
                        mat[p[0]][p[1]] = 1


def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()


if __name__ == "__main__":
    p1, p2 = (0, 0), (0, 0)
    for i in range(len(MAT)):
        for j in range(len(MAT[0])):
            if MAT[i][j] == 8:
                p1 = (i, j)
            elif MAT[i][j] == 9:
                p2 = (i, j)

    check(MAT, p1, p2)
    print_mat(MAT)

