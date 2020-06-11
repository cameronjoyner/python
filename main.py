
def printGrid(grid):
    row = ""
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                row += str(grid[i][j]) + " "
            else:
                row += "_" + " "
        print(row)
        row = ""

def safeRow(grid, rowIdx, number):
    for i in range(9):
        if grid[rowIdx][i] == number:
            return True
    return False

def safeCol(grid, colIdx, number):
    for j in range(9):
        if grid[j][colIdx] == number:
            return True
    return False

def safeBox(grid, row, col, number):
    for i in range(3):
        for j in range(3):
            if grid[i + row][j + col] == number:
                return True
    return False



def findEmpty(grid, lst):
    for row in range(9):
        for col in range(9):
            #print(arr[row][col])
            if grid[row][col] == 0:
                lst[0] = row
                lst[1] = col
                return True
    return False


def checkIfSafe(grid, row, col, num):
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not safeRow(grid, row, num) and not safeCol(grid, col, num) and not safeBox(grid, row - row % 3, col - col % 3, num)

def solve(grid):
    lst = [0, 0]

    # If there is no unassigned location, we are done
    if not findEmpty(grid, lst):
        #print("no unassigned location!")
        return True

    row = lst[0]
    col = lst[1]

    for num in range(1,10):

        # if looks promising
        if checkIfSafe(grid, row, col, num):

            grid[row][col] = num
            print("here for " + str(grid[row][col]))

            if solve(grid):
                return True

        grid[row][col] = 0

    #trigger backtrack
    return False

grid =[[0 for x in range(9)]for y in range(9)]

grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

printGrid(grid)
print(str(safeRow(grid,0,4)) + " for the row " + str(list(grid[0])))
print(str(safeCol(grid,0,9)) + " for the row zero")
print(str(safeBox(grid,0,0,2)) + " for the first box")
print(str(checkIfSafe(grid,0,0,2)))

#print(str(findEmpty(grid,[0,0])))

if solve(grid):
    printGrid(grid)
else:
    print("No solution exists")