def findRedundantConnection(edges):

    redundant = []

    node_2 = set()

    for edge in edges:

        if edge[1] in node_2:

            redundant.append(edge)
        
        else:

            node_2.add(edge[1])

    return redundant[-1]

# Example usage:
if __name__ == "__main__":

    edges = [[1, 2], [1, 3], [2, 3]]

    print(findRedundantConnection(edges))

    edges = [[1,2],[2,3],[3,4],[1,4],[2,4],[2,5],[1,5]]

    print(findRedundantConnection(edges))