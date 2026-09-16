from collections import deque

def bfs(graph, source):
    """Find the path with the fewest edges from source to every vertex it can reach.

    Dijkstra's algorithm answers "cheapest route" using the edge weights. This one
    answers "fewest stops" instead, so the weights are ignored. The two disagree
    whenever a longer chain of cheap edges beats one expensive edge.

    Returns (hops, path), the same shape sp.dijkstra returns: hops[v] is the number
    of edges to reach v, and path[v] is the list of vertices visited before v.
    """
    hops = {source: 0}
    path = {source: []}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        # graph.get(u, {}) because a vertex with no outgoing edges has no key
        for v in graph.get(u, {}):
            if v not in hops:
                hops[v] = hops[u] + 1
                path[v] = path[u] + [u]
                queue.append(v)

    return hops, path
