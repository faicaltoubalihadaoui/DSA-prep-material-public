def bellman_ford(n, edges, src):
    distances = [float("Inf")] * n
    distances[src] = 0

    for i in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float("Inf") and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in edges:
        if distances[u] != float("Inf") and distances[u] + w < distances[v]:
            return -1

    return distances


# what it does ?

#
