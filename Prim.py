import heapq


def Prim(s, graph):
    # Priority queue to store (weight, from_node, to_node)
    pq = [(0, s, s)]
    visited = set()
    mst = []

    while pq:
        weight, from_node, to_node = heapq.heappop(pq)

        # If the to_node is already visited, we skip this edge
        if to_node in visited:
            continue

        visited.add(to_node)

        # We add the edge to the MST, but we skip the initial edge (0, start_node, start_node)
        if from_node != to_node:
            mst.append((from_node, to_node, weight))

        # Add all edges from the to_node to the priority queue
        for neighbor, edge_weight in graph[to_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, to_node, neighbor))

    return mst
