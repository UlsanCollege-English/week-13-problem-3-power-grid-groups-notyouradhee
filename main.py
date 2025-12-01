

def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # TODO Step 1–3: Make sure you understand "power group" and the inputs/outputs.
    # TODO Step 4: Decide how to store neighbors (graph representation).
    # TODO Step 5: Write pseudocode for traversing the graph and counting groups.
    # TODO Step 6: Implement a graph traversal (DFS or BFS) to explore groups.
    # TODO Step 7: Test on small graphs (1 node, chain, completely separate nodes).
    # TODO Step 8: Check that your solution is roughly O(n + m).
    visited = set()
    station_set = set(stations)
    graph = {s: set() for s in stations}
    for a, b in lines:
        if a in station_set and b in station_set:
            graph[a].add(b)
            graph[b].add(a)
    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for nei in graph.get(node, ()):    
                if nei not in visited:
                    stack.append(nei)
    count = 0
    for s in stations:
        if s not in visited:
            dfs(s)
            count += 1
    return count


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
