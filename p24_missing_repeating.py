def findMissingAndRepeatedValues(grid):

    n = (len(grid) * len(grid[0])) + 1

    res = [i for i in range(1, n)]

    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if grid[i][j] not in res:

                res.insert(0, grid[i][j])

            else:

                res.remove(grid[i][j])

    return res

if __name__ == "__main__":

    grid = [[9,1,7],[8,9,2],[3,4,6]]

    findMissingAndRepeatedValues(grid)