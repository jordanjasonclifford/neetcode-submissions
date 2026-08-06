class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Build an adjacency list:
        # each node maps to all nodes directly connected to it
        graph = [[] for _ in range(n)]

        # The graph is undirected,
        # so every edge must be stored in both directions
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Track which nodes have already been visited
        visited = [False] * n

        def dfs(node):
            # Explore every neighbor connected to the current node
            for neighbor in graph[node]:

                # Only visit each node once
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        # Count how many separate connected groups exist
        components = 0

        # Check every node in case the graph has disconnected sections
        for node in range(n):

            # An unvisited node begins a new connected component
            if not visited[node]:
                visited[node] = True

                # Visit every node connected to this starting node
                dfs(node)

                # One complete connected component was found
                components += 1

        return components