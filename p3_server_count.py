def countServers(grid):

    rows, cols = len(grid), len(grid[0])

    visited = set()

    servers = set()

    for i in range(rows): 
        
        for j in range(cols):

            if grid[i][j] == 1:

                servers.add((i, j))

    for server in servers:

        neighbor_found = 0

        r, c = server

        for i in range(rows):

            if grid[i][c] == 1 and (i, c) != server:

                neighbor_found = 1

                visited.add((i, c))

        for i in range(cols): 

            if grid[r][i] == 1 and (r, i) != server:

                neighbor_found = 1

                visited.add((r, i))
        
        if neighbor_found == 1:

            visited.add(server)

    return len(visited)

if __name__ == "__main__":

    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

    print(countServers(grid)) # Output:4