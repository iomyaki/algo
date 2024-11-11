"""
Graph is given by the adjacency matrix. For example, vertex #1 is connected to vertices #2, #3, and #5.
At time 0, each vertex of the graph contains one microbe. Then every second the following happens:
each microbe at each vertex is divided into d microbes (d is the degree of the vertex), and one copy jumps over all
neighbors of the vertex (there is no microbe left at the vertex itself).
How many microbes will be in the first vertex of the graph after 16 seconds?
"""

import numpy as np
from copy import deepcopy


adjacency_initial = np.array([[0, 1, 1, 0, 1, 0],
                              [1, 0, 0, 1, 1, 0],
                              [1, 0, 0, 0, 1, 1],
                              [0, 1, 0, 0, 0, 1],
                              [1, 1, 1, 0, 0, 1],
                              [0, 0, 1, 1, 1, 0]
                              ])

state = np.array([1, 1, 1, 1, 1, 1])
adjacency = deepcopy(adjacency_initial)
for _ in range(16):
    for i in range(6):
        adjacency[i] = np.multiply(adjacency[i], state[i])

    state = np.sum(adjacency, axis=0)
    adjacency = deepcopy(adjacency_initial)

print(state[0])
