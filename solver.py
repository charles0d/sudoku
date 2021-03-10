import numpy as np


def valid(array):
    for i in range(9):
        if (not checkBlock(square(array, i)) or
                not checkBlock(array[i, :]) or
                not checkBlock(array[:, i])):
            return False
    return True


def validTrial(array, r, c, trial):
    array[r, c] = trial
    squareNumber = 3 * (r // 3) + c // 3
    res = checkBlock(row(array, r))
    res = res and checkBlock(column(array, c))
    res = res and checkBlock(square(array, squareNumber))
    array[r, c] = 0
    return res


def square(array, i):
    """ Squares are numbered from left to right first
        and then from top to bottom.
        ex: square 3 is middle left.
    """
    r, c = 3 * (i // 3), 3 * (i % 3)
    rows = [r, r + 1, r + 2]
    cols = [c, c + 1, c + 2]
    return [array[i, j] for i in rows for j in cols]


def row(array, i):
    return array[i, :]


def column(array, i):
    return array[:, i]


def checkBlock(block):
    blockWo0 = [n for n in block if n != 0]
    return len(blockWo0) == len(set(blockWo0))


def solve(current, solution):
    workCurrent = np.copy(current)
    i, j = np.where(workCurrent == 0)
    if len(i) == 0:
        for r in range(9):
            for c in range(9):
                solution[r, c] = workCurrent[r, c]
        return
    else:
        for trial in range(1, 10):
            workCurrent[i[0], j[0]] = trial
            # TODO:  check only 3 blocks with validTrial
            if valid(workCurrent):
                solve(workCurrent, solution)


m = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
     [5, 2, 0, 0, 0, 0, 0, 0, 0],
     [0, 8, 7, 0, 0, 0, 0, 3, 1],
     [0, 0, 3, 0, 1, 0, 0, 8, 0],
     [9, 0, 0, 8, 6, 3, 0, 0, 5],
     [0, 5, 0, 0, 9, 0, 6, 0, 0],
     [1, 3, 0, 0, 0, 0, 2, 5, 0],
     [0, 0, 0, 0, 0, 0, 0, 7, 4],
     [0, 0, 5, 2, 0, 6, 3, 0, 0]]

blank = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

ez1 = np.array([[0, 4, 8, 0, 0, 0, 0, 7, 0],
                [2, 7, 0, 6, 9, 0, 0, 3, 0],
                [0, 3, 0, 0, 7, 2, 0, 4, 0],
                [3, 8, 7, 9, 2, 0, 4, 1, 5],
                [4, 9, 2, 1, 0, 8, 7, 6, 3],
                [5, 1, 6, 0, 4, 0, 9, 2, 8],
                [0, 2, 3, 4, 6, 9, 1, 5, 0],
                [7, 5, 4, 2, 8, 1, 3, 0, 6],
                [1, 6, 9, 7, 3, 5, 0, 0, 0]])

print(valid(np.array(m)))
print(validTrial(ez1, 0, 0, 2))

solution = np.zeros((9, 9))
solve(ez1, solution)
print(solution)
solve(np.array(m), solution)
print(solution)
