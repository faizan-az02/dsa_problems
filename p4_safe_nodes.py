def eventualSafeNodes(graph):

    terminal_nodes = set()

    safe_nodes = []

    for i, connections in enumerate(graph):

        if len(connections) == 0:

            terminal_nodes.add(i)

    print(terminal_nodes)

    for i, connections in enumerate(graph):

        if len(connections) == 1:
            
            if connections[0] in terminal_nodes:

                safe_nodes.append(i)

    safe_nodes.extend(terminal_nodes)

    return sorted(safe_nodes)

if __name__ == "__main__":

    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(eventualSafeNodes(graph)) # Output: [2,4,5,6]
